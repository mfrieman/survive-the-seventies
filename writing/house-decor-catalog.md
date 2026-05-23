# 70s House Decor Stereotype Catalog

This catalog is the visual identity system for every important household in **Survive the 70s**. Each home gets exactly **one** exaggerated 1970s decor stereotype as its identity. The stereotype is doing double duty:

- **For Gen X players:** "Oh god, I remember that exact couch."
- **For Gen Z players:** "Wait, people *chose* this?"

Both reads land. That's the design goal.

## How places reference this

In `writing/intake/places.yaml`, each home entry has a `decor_style:` field pointing at one of the IDs below. The catalog entry is the source of truth for what the room looks/smells/feels like — the place entry just inherits and adds location-specific extras (e.g., "same look, but trashed").

## Rules

1. **One stereotype per household — with one exception.** No mixing across the public spaces of a house. The whole house commits to the bit. EXCEPTION: **kid bedrooms are sovereign territory.** A 14-year-old does not decorate to match Mom's bicentennial parlor or Mom's Greek Orthodox icon corner. Kid bedrooms get their own micro-stereotypes (see "Kid Bedroom Variants" below) layered OVER the house's bones (the wood paneling, the carpet, the shag — those stay).
2. **Period-accurate first, exaggerated second.** Everything has to have actually existed in 1976; we then dial it to 11.
3. **Smell matters.** Every entry includes a smell line. The 70s smelled specific.
4. **The bit can survive damage.** If a Greek Orthodox Maximalist couch ends up in a garage getting destroyed for a decade, it's still Greek Orthodox Maximalist — just ruined. The stereotype reads through the damage.

---

## Catalog

### `greek-orthodox-maximalist` — the Karras style
**Vibe:** A devout Greek-American mom in her late 30s redid the living room in 1965 with the most "tasteful" furniture the Sears catalog could offer, and has not redecorated since.

**Walls:** Wood paneling halfway up, textured cream wallpaper above. Gold-haloed icons of Christ, the Theotokos, and Saint Nicholas in every room. A small *mati* (blue evil-eye charm) hung over every doorway and pinned inside the kids' jacket collars. A framed icon of the Mystical Supper above the dining table. A small Greek flag on a stand near the front door. Cluster of family portraits arranged like a shrine — kids' baptisms, wedding photos, grandparents back in Thessaloniki.

**Furniture:** Heavy dark wood. Carved feet. The good couch is a floral-print sofa — burgundy, gold, and forest-green flowers on a cream background — with crocheted antimacassars pinned to the armrests and the headrest. Matching wingback chair. Marble-top end tables. A china cabinet you do not touch under any circumstances.

**Floor:** Wall-to-wall harvest-gold carpet upstairs. A *flokati* (machine-made cousin of the real thing) under the dining table. Plastic floor runners protecting traffic paths.

**Soft goods:** Doilies on every flat surface. Plastic slipcovers on the formal-living-room furniture that nobody is allowed to sit on. Lace curtains layered under heavier drapes.

**Lighting:** Big amber-glass hanging fixture over the dining table. Table lamps with pleated shades. A vigil lamp (*kandili*) burning red oil in front of the family icon corner. Always a little dim.

**Decorative objects:** Glass grapes in a cut-glass bowl. A small fountain that doesn't run. Worry beads (*komboloi*) hung from a hook by the front door. Saint-figurine collection in a corner cabinet. Candy dish full of *koufeta* (Jordan almonds) that have fused into one mass.

**Smell:** Garlic, oregano, lemon, olive oil, Pine-Sol, and a faint backbeat of frankincense from the Sunday censing.

**Sound:** A clock that ticks too loud. Greek-language AM radio on Sunday mornings. Lawrence Welk Saturdays if Costas "Gus" is in the recliner.

**Cleanliness:** Spotless. Vacuumed daily. The plastic slipcovers squeak when you sit down.

**The joke:** This is hand-built for Athena Karras. It also describes The Dungeon — because the Dungeon's furniture is the *previous* iteration of this same set, sent out to the garage and destroyed by ten years of teenagers.

---

### `colonial-american-bicentennial` — the Marek style
**Vibe:** A working-class Baltimore-county family that redid the living room for the 1976 Bicentennial and went ALL the way. They love their country and they love a sale at Sears.

**Walls:** Wood paneling at chair-rail height, eggshell or cream above. A framed cross-stitch of the Liberty Bell. A small bald eagle plaque. A framed print of the signing of the Declaration. A "Don't Tread On Me" novelty hand towel hanging in the kitchen that nobody actually uses.

**Furniture:** The "parlor set" — high-backed wingback sofa with exposed solid-maple frame, knotty-pine accents, carved feet, and visible wooden spindles. Upholstered in a busy floral or plaid corduroy: harvest gold, burnt orange, chocolate brown, avocado green. Matching wingback chairs. A heavy maple coffee table with a turned-spindle base and the same Colonial silhouette. In the dining room: a wagon-wheel chandelier (real wood, fake candle bulbs) and a maple table that seats six with matching captain's chairs.

**Floor:** Wall-to-wall harvest-gold or burnt-orange shag in the living room. Fake-brick-pattern linoleum in the kitchen. A braided oval rag rug in the foyer.

**Soft goods:** Plaid throw pillows. A patchwork quilt over the back of one chair. No plastic slipcovers (this isn't the Karrases) — the furniture is meant to be used.

**Lighting:** The wagon-wheel chandelier (load-bearing visual). Table lamps with milk-glass globes or pleated burlap shades. A wall sconce with a hurricane chimney.

**Decorative objects:** A hutch full of Bicentennial commemorative plates that Kay actually uses for Sunday dinner. A bald eagle decanter on the console TV (never opened). A cast-iron eagle bottle opener mounted next to the back door. A small American flag on a stand near the front window.

**Smell:** Brewed coffee, Kool 100s, joint compound on Dennis's work clothes, whatever Kay's actually cooking (unlike the Karras kitchen, this one delivers).

**Sound:** The Precedent Stereophonic Recordergram playing Motown loud enough to embarrass the neighbors. The console TV under it. Kay's voice over both of them.

**Cleanliness:** Lived-in. Kay keeps it nice but doesn't fuss. There are coasters; there are also rings on the coffee table that have been there since '73.

**The joke:** Maximum sincere patriotism filtered through Sears catalog choices. The Mareks committed to the bit and the bit is still committed to them three years past peak Bicentennial. Beneath the eagle decanter and the wagon-wheel chandelier, a Black-music-loving white mother is blasting The Temptations next to a flag she means with her whole heart.

---

### `hippie-crash-pad` *(planned — for future character)*
**Vibe:** A 28-year-old who never quite came home from the commune.

**Walls:** Tapestries — Indian print, mandalas, a Bob Dylan poster, a Che Guevara silkscreen, a Jimi at Monterey. Beaded curtain in every doorway. A wall-mounted black-light poster of a tiger that nobody admits to liking.

**Furniture:** Floor cushions. A bean bag chair. A shag-upholstered "conversation pit" couch in burnt orange. Egg chair. Macrame plant hangers everywhere.

**Floor:** Long shag carpet, harvest gold or avocado, badly maintained. Throw rugs layered.

**Lighting:** Lava lamp. String lights year-round. Candles burning even when nobody's there to watch them, which is concerning.

**Decorative objects:** Hookah you're told is "for tobacco." A wall of records. A coffee table made from a wire spool. Houseplants — including one suspicious one in the corner.

**Smell:** Patchouli, sandalwood incense, weed, and lentils.

**Sound:** Either total silence or a Pink Floyd album played in its entirety.

**Cleanliness:** Not exactly dirty, but not clean either. There is a layer.

**The joke:** Painful sincerity. Will explain his stuff.

---

### `disco-glam` *(planned — for future character)*
**Vibe:** A childless adult couple, mid-30s, who saw *Saturday Night Fever* and built their entire identity around it.

**Walls:** Mirrored panels on at least one wall. Silver foil wallpaper. Lucite-framed prints of jazz musicians.

**Furniture:** Black leather sofa. White shag accent. Lucite/acrylic coffee table. Chrome bar cart, fully stocked. Mirrored dining table.

**Floor:** White carpet (a war crime). Or black-and-white checkerboard linoleum in entry/kitchen.

**Lighting:** Track lighting. A small mirror ball over the bar cart. Pink neon "BAR" sign.

**Decorative objects:** Brass swan. A real Lucite chess set nobody plays. Framed concert tickets. A Sansui silver-faced stereo nicer than your car.

**Smell:** Aqua Velva, hairspray, cigarettes (long cigarettes, in a long holder), and Chivas.

**Sound:** KC and the Sunshine Band on continuous loop. The wife's heels on the linoleum.

**Cleanliness:** Compulsively clean — everything wipes down.

**The joke:** Try-hard cool. They want you to compliment something so they can tell you what it cost.

---

### `wood-paneling-everyman` *(planned — for the Marek house, probably)*
**Vibe:** Middle-of-the-bell-curve American family. Did the basement themselves. Didn't try to be anything.

**Walls:** Wood paneling top to bottom (real plywood paneling, dark walnut tone). A few framed photos. A starburst clock from Sears.

**Furniture:** Earth-tone plaid couch. La-Z-Boy recliner. A console TV that's also a piece of furniture.

**Floor:** Wall-to-wall harvest-gold or burnt-orange shag.

**Decorative objects:** A bowl of those clear-glass candies on the coffee table. A magazine rack with TV Guide and Reader's Digest.

**Smell:** Coffee, cigarettes, and whatever's for dinner.

**Sound:** The TV, always.

**Cleanliness:** Lived-in. Mom keeps it nice.

**The joke:** The joke is that there is no joke. This is the baseline against which every other house reads as exaggerated.

---

## Stereotypes still to add as needed

When a new character is introduced, we'll add their household stereotype here. Candidates already in the writing room:

- **Hunting-Lodge Patriot** — Dad who voted for Nixon twice, bear rug, deer head, framed flag, gun cabinet, Field & Stream
- **Tiki Lounge Suburbanite** — Couple obsessed with Hawaii after one trip, fake bamboo, plastic leis, a real backyard tiki bar
- **Ranch-and-Macrame Single Mom** — Divorced in '74, owl macrame, beige everything, a single afghan throw, a self-help paperback always face-down on the couch
- **Trailer Modular** — Wood-grain Formica, popcorn ceiling, beanbag, console stereo as the centerpiece, dim
- **Mid-Century Holdout** — Older couple, never updated past 1962, Eames-adjacent furniture that's now genuinely cool but they don't know it
- **Bachelor Pad Catastrophe** — Divorced dad living in a one-bedroom over the bowling alley, TV tray dining, one fork

The catalog is open-ended. Add as needed.

---

## Kid Bedroom Variants

Kid bedrooms are an exception to Rule #1. The house's bones come through (wood paneling, shag carpet, the original closet door) but the walls, the bed, the desk, and the air are the kid's. Pick the variant that matches the kid.

### `bedroom-rocker` — for the music-obsessed teen
**Walls:** KISS BLAZE poster over the bed. Aerosmith *Rocks* on the closet door. A pull-out *Creem* magazine centerfold of Mickey's actual guitar hero. A black-and-white concert photo torn out of *Circus* and taped up uneven. A peace sign drawn in Sharpie on the back of the door. Wood paneling shows through wherever there's no poster.
**Bed:** Twin with a brown plaid bedspread that has been worn smooth.
**Desk/floor:** A clock radio permanently tuned to WBAY-FM. *MAD* and *National Lampoon* on the nightstand. Hi-fi headphones with a coiled cord that reaches the bed. Cassette tapes loose on every surface. A guitar in the corner — possibly played, possibly decoration.
**Smell:** Old Spice, sneakers, faint mildew from a damp towel he forgot.
**Sound:** The clock radio at all hours. Sometimes Mickey-from-down-the-block on the closet record player.
**Use for:** Danny, Mickey (if Mickey ever had a bedroom — he doesn't, he has the Dungeon)

### `bedroom-farrah-and-football` — for the jock/popular boy
**Walls:** Farrah Fawcett red-swimsuit poster (the poster of the era). A pennant for the local team. A photo of a babysitter the kid is in love with, stolen. A trophy shelf with three actual trophies and four participation ribbons.
**Bed:** Twin with a striped sheet set. A football helmet on the bedpost.
**Floor:** A practice football. Cleats. A baseball glove with a ball tied into it overnight.
**Smell:** Tiger Balm, deodorant the kid doesn't quite know how to use yet, the football.
**Sound:** A radio tuned to Orioles games in season.
**Use for:** the cool older kid down the street, the bully's "good" brother

### `bedroom-blacklight-felt` — for the burnout-in-training
**Walls:** Black-light posters of mushrooms, dragons, and naked women obscured by said dragons. A Cheech & Chong *Big Bambu* album cover thumbtacked up. A black-light tube replacing the regular bulb in the desk lamp. A Pink Floyd *Dark Side* prism poster.
**Bed:** Tangle of brown sheets. A waterbed if the kid's parents are dumb enough.
**Floor:** Incense ash. A roach clip pretending to be a feather earring. The empty cardboard sleeve of a record but no record. A pipe the kid swears is "just for tobacco."
**Smell:** Strawberry incense laid over weed laid over weed.
**Sound:** Either silence or Floyd, both at low volume.
**Use for:** the older brother of one of Danny's friends, a Catholic-school kid Mickey knows

### `bedroom-little-kid` — for the under-10
**Walls:** Storybook Hollow characters on every available surface. The lunchbox displayed on the dresser. Construction-paper crafts taped up at adult-eye-height. One stray Han Solo poster (parody name TBD) that he's too cool to take down even though he's 7.
**Bed:** Twin with the Storybook Hollow sheets. Stuffed animals in the regulation pyramid against the headboard.
**Floor:** Lincoln Logs that have spread to occupy 60% of the floor. Matchbox cars. One sad Stretch Armstrong, leaking corn syrup.
**Smell:** Crayons, kid sweat, the inside of the lunchbox after a long week.
**Sound:** AM radio at 6 AM on Saturday — Storybook Hollow cartoons.
**Use for:** Bobby Marek

### `bedroom-girl-disco` — for the older sister/teenage girl on the block
**Walls:** Shaun Cassidy. David Cassidy. *Tiger Beat* tear-outs taped in collage. Mirror with stickers around the edge.
**Bed:** Canopy if Daddy splurged. Quilted floral comforter.
**Floor:** A record player on the floor with a stack of 45s. A roller skate on its side. A pile of *Seventeen*.
**Smell:** Love's Baby Soft, Bonne Bell Lip Smackers (strawberry), Aqua Net.
**Sound:** The Bee Gees, the Captain & Tennille, ABBA.
**Use for:** future older-sister characters; Iwona's room? (see her own entry — she may break this stereotype on purpose)

---

## Destination Decor Stereotypes

These follow the same format as household stereotypes but for non-residential locations. Each destination gets one.

---

### `cheap-regional-amusement-park-1976` *(Storybook Hollow)*
**Vibe:** A storybook-theme park built in 1956 by a guy who had two ideas and three buckets of paint. Twenty years of weather later. Disney-adjacent in the way a knockoff watch is Rolex-adjacent. Beloved by 7-year-olds, dreaded by everyone over 12, lawsuit-bait to OSHA.

**Color Palette:** Sun-faded primary colors — robin's-egg blue, daffodil yellow, sun-bleached cherry red, peeling white. The paint hasn't been touched since '61. The pond is brown.

**Materials:**
- Plywood. Plywood everywhere. Plywood castles, plywood cottages, plywood mice.
- Concrete block painted to look like stone. Visible mortar joints.
- Plaster figures with the rebar showing through where a kid grabbed a hand off in 1971.
- Asphalt paths cracked into puzzle pieces by twenty Maryland winters.
- Steel — exposed, unpadded, oxidized — on every railing, slide, swing, and ride.
- Gas-powered ride engines. They are not tuned.

**Signage:** Hand-painted. Comic Sans before Comic Sans. The "i" in *Storybook* has a star instead of a dot. Half the signs have a faded "BUY YOUR STORYBOOK HOLLOW PHOTO!" sticker on them.

**Smell:** Hot tar from the asphalt, popcorn, pond water (specifically pond water), warm rubber from the antique-car tires, the petting-zoo deer, cotton candy.

**Sound:** Loudspeaker pole near the snack bar playing scratchy nursery-rhyme music on an endless loop. Tugboat engine sputtering. The screams of children — sometimes joyful, sometimes the other kind, you cannot tell which from a distance. Cicadas. The metallic clang of the Mother Goose ride hitting its end-of-track bumper.

**Lighting (day):** Brutal Maryland summer sun. No shade except inside Willie the Whale.

**Lighting (night):** One amber service light by the snack bar. Everything else is just shapes against the moon. The painted dwarves are worse in the dark. So is Willie.

**Safety Features:** None to speak of. The metal slide is the temperature of a frying pan. The boats have no life jackets. The cars have no seat belts and no center barrier. The petting zoo deer have antlers. The moon bounce hasn't been cleaned since the Carter administration.

**Cleanliness:** Garbage cans full, then overflowing, by noon on a Saturday. The moon bounce has a permanent black film. The snack-bar floor has a topology.

**The joke (DAYTIME):** This is fun! The kids are having a great time! Three of them are bleeding!

**The joke (NIGHTTIME):** The painted dwarves were creepy in daylight. With one service light and a moon, they're a horror movie. Willie the Whale's mouth is now a mouth.

**Use for:** Storybook Hollow (the only destination with this stereotype — built for it). Distinct daytime and nighttime moods.

---

### `scandinavian-modern-european-overlay` *(the Kowalski house)*
**Vibe:** A Polish-American homemaker (Mary Kowalski) trying — and largely succeeding — at making a 1920s Baltimore brick rowhouse look like a stylish Stockholm or Warsaw apartment. The bones are working-class American; the surfaces are deliberate, light, sparse, intentional. Reads to American neighbors as "interesting" and slightly intimidating. Reads to a Polish visitor as "she's trying so hard, and she's actually doing it."

**Color Palette:** Whites, creams, pale wood, mustard yellow, a single bold accent (a Marimekko orange or a Finnish cobalt). Earth tones grounded but not dominant. The opposite of harvest-gold/avocado American 70s.

**Materials:**
- Danish teak — coffee table, sideboard, dining chairs. Real teak, polished weekly.
- White-painted plaster walls (rare in this neighborhood — the other houses have wood paneling or wallpaper).
- Linen and natural fiber throws, never plastic slipcovers.
- Tile floor in the foyer; hardwood elsewhere, scrubbed.
- Brass and ceramic, never plastic.

**Furniture / Layout instincts:**
- Lower furniture than American norm — Scandinavian designers cut couches and chairs an inch or two shorter.
- *Negative space.* Mary leaves walls bare where an American neighbor would hang four things. The one thing she does hang is centered and matters.
- A "front sitting room" kept perfectly clean, off-limits, used only for parties. (Classic Polish/Eastern European household rule — preserved from the old country.)

**Art:**
- One framed cross-stitched landscape of the Tatra Mountains.
- One Marimekko print (the orange poppy) hung in the kitchen.
- A small icon corner — modest, not maximalist like the Karras house. Polish Catholic, not Greek Orthodox: a single Black Madonna of Czestochowa print and a candle.
- Peter's paintings on a few walls — landscapes, Old Country and New, in progress.

**Smell:** Wood polish (used weekly), fresh bread (Mary bakes Saturdays), instant coffee, faintly pierogi from Maggie's eternal pot.

**Sound:** Polish-language AM radio on top of the fridge. Peter's accordion from the back room. Natan's record player upstairs (probably David Bowie, probably Roxy Music). The Polish + English code-switching of three generations talking past each other in the kitchen.

**Cleanliness:** Compulsive. Mary keeps it spotless and resents (silently) that she does it alone.

**The joke:** A European woman ferociously curating a European-looking life inside the brick shell of a Baltimore rowhouse, while her husband quietly drinks himself blurry in the basement and her senile mother calls everyone the wrong name with total affection. The aesthetic is real. The chaos underneath is also real. Both can be true.

**Use for:** Kowalski household ONLY. The European-overlay-on-rowhouse aesthetic is specific to Mary; nobody else on the block is trying anything like this.
