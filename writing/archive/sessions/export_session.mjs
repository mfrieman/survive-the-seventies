/**
 * Export a single Clawpilot session transcript to Markdown.
 *
 * Usage:
 *   node export_session.mjs <session_id> <output_markdown_path>
 *
 * Reads from ~/.copilot/session-store.db and writes a clean Markdown transcript
 * that's independent of Clawpilot. Suitable for committing to git and reading
 * by other LLMs.
 *
 * Requires Node 22+ with --experimental-sqlite flag (built-in SQLite).
 */
import { DatabaseSync } from "node:sqlite";
import { mkdirSync, writeFileSync, statSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { homedir } from "node:os";

const DB_PATH = resolve(homedir(), ".copilot", "session-store.db");

function quote(s) {
  if (!s) return "_(empty)_";
  return "```\n" + s.trimEnd() + "\n```";
}

function exportSession(sessionId, outPath) {
  const db = new DatabaseSync(DB_PATH, { readOnly: true });

  const sess = db
    .prepare(
      "SELECT id, summary, cwd, repository, branch, created_at, updated_at FROM sessions WHERE id = ?"
    )
    .get(sessionId);

  if (!sess) {
    console.error(`Session not found: ${sessionId}`);
    process.exit(1);
  }

  const turns = db
    .prepare(
      "SELECT turn_index, user_message, assistant_response, timestamp FROM turns WHERE session_id = ? ORDER BY turn_index"
    )
    .all(sessionId);

  const checkpoints = db
    .prepare(
      "SELECT checkpoint_number, title, overview, work_done, technical_details, important_files, next_steps FROM checkpoints WHERE session_id = ? ORDER BY checkpoint_number"
    )
    .all(sessionId);

  const filesTouched = db
    .prepare(
      "SELECT DISTINCT file_path, tool_name FROM session_files WHERE session_id = ? ORDER BY file_path"
    )
    .all(sessionId);

  db.close();

  mkdirSync(dirname(outPath), { recursive: true });

  const parts = [];
  parts.push(`# Session Transcript — ${sessionId}\n`);
  parts.push(`- **Exported:** ${new Date().toISOString()}`);
  parts.push(`- **Created:** ${sess.created_at}`);
  parts.push(`- **Updated:** ${sess.updated_at}`);
  parts.push(`- **Working Dir:** \`${sess.cwd}\``);
  if (sess.repository) {
    parts.push(`- **Repo:** \`${sess.repository}\` (branch: \`${sess.branch}\`)`);
  }
  parts.push(`- **Turn Count:** ${turns.length}\n`);
  parts.push("---\n");

  if (checkpoints.length) {
    parts.push("## Checkpoints\n");
    for (const cp of checkpoints) {
      parts.push(`### Checkpoint ${cp.checkpoint_number} — ${cp.title}\n`);
      if (cp.overview) parts.push(`**Overview:**\n\n${cp.overview}\n`);
      if (cp.work_done) parts.push(`**Work Done:**\n\n${cp.work_done}\n`);
      if (cp.technical_details) parts.push(`**Technical Details:**\n\n${cp.technical_details}\n`);
      if (cp.important_files) parts.push(`**Important Files:**\n\n${cp.important_files}\n`);
      if (cp.next_steps) parts.push(`**Next Steps:**\n\n${cp.next_steps}\n`);
    }
    parts.push("---\n");
  }

  if (filesTouched.length) {
    parts.push("## Files Touched This Session\n");
    for (const ft of filesTouched) {
      parts.push(`- \`${ft.file_path}\` (${ft.tool_name})`);
    }
    parts.push("\n---\n");
  }

  parts.push("## Transcript\n");
  for (const t of turns) {
    parts.push(`### Turn ${t.turn_index}  *(${t.timestamp})*\n`);
    parts.push("**User:**\n");
    parts.push(quote(t.user_message));
    parts.push("\n**Assistant:**\n");
    parts.push(quote(t.assistant_response));
    parts.push("\n---\n");
  }

  writeFileSync(outPath, parts.join("\n"), "utf-8");
  const size = statSync(outPath).size;
  console.log(`Wrote ${outPath} (${size.toLocaleString()} bytes, ${turns.length} turns)`);
}

const [, , sessionId, outPath] = process.argv;
if (!sessionId || !outPath) {
  console.error("Usage: node export_session.mjs <session_id> <output_path>");
  process.exit(1);
}
exportSession(sessionId, resolve(outPath));
