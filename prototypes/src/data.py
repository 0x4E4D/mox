# Content copied word for word from moxsf.com (Nov 2026).
TAGLINE = 'A research-focused incubator &amp; community space for <em>doers of good</em> and <em>masters of craft</em>.'
ADDRESS = '1680 Mission Street, San Francisco'
EVENTS = [("WED","4pm","Mox-Giving"),("WED","5pm","AI-Philosophy Writing Group"),("FRI","6pm","Band Setup + Practice"),("SAT","7pm","Mox-tunies! Live Band Karaoke"),("MON","7pm","SF Lean Meetup")]
GATHER = ["Startup founders","Effective altruists","Alignment researchers","Filmmakers","Writers","Musicians","Community builders","Hackers","Designers","Gamers"]
STAFF = [
 ("austin-chen","CEO OF MANIFUND","Austin Chen","effective altruism funding","Catholic faith &amp; philosophy",["Strategic Partnerships","Custom Requests"],"austin@moxsf.com"),
 ("leilani-bellamy","DIRECTOR","Leilani Bellamy","Art of Accomplishment","niche bodywork",["Strategic Partnerships","Custom Requests","Events","Private Offices"],"leilani@moxsf.com"),
 ("carolina-oliveira","COMMUNITY AND FELLOWSHIPS","Carolina Oliveira",None,None,["Global Expert Fellowship","Events","Fellowships","Strategic Partnerships","Membership","Private Offices"],"carolina@moxsf.com"),
 ("robin-goins","HEAD OF OPERATIONS","Robin Goins","understanding understanding",None,["Venue Rental","Private Offices","Events","Membership","Member Events","Event support"],"robin@moxsf.com"),
]
MEMBERS = [
 ("lily-shi","Lily Shi","LLM interpretability","dance","Pivotal Fellows"),
 ("jez-ng","Jez Ng","building the fastest mach-o linker","growing mushrooms","Members"),
 ("kara-presbrey","Kara Presbrey","aligned BCI","scuba diving","Members"),
 ("haoxing-du","Haoxing Du","real-world agent traces","paragliding","Surplus"),
 ("kris-gulati","Kris Gulati","economics of AI","origami","Members"),
 ("leona-mollica","Leona Mollica","Decision theory foundations","Calligraphy","Members"),
 ("timothy-zhou","Timothy Zhou","LLM jailbreak interpretability","composing chamber music","Members"),
 ("helen-tsim","Helen Tsim","AI safety communications","Improv Comedy","The Frame"),
 ("ran-sun","Ran Sun","US/China AI Safety Coordination","Rock Climbing","Members"),
 ("william-jarrold","William Jarrold","Mechanistic Interpretability","Jazz Piano","Members"),
 ("avi-sundaresan","Avi Sundaresan","world-state compression","espresso","Talarion"),
 ("tomas-guarna","Tomás Guarna","Anthropology+History of Safety","Typefaces","Members"),
 ("max-feldman","Max Feldman","Software Verification","Distance Running","Members"),
 ("aidan-kankyoku","Aidan Kankyoku","AI for animal welfare","Japanese tea ceremony","Sentient Futures"),
 ("peter-chatain","Peter Chatain","agent foundations","olympic rowing","Members"),
 ("christine-shiba","Christine Shiba","social infrastructure","climbing","Surplus"),
 ("julie-steele","Julie Steele","AI safety","dancing","Members"),
 ("keshav-shenoy","Keshav Shenoy","aligning ai models","birds","Members"),
 ("alan-tan","Alan Tan","value learning","advanced meditation","Members"),
 ("hudson-mitchell-pullman","Hudson Mitchell-Pullman","learning science","coffee (oatmilk lattes)","Surplus"),
]
# (file, label shown as text beside the mark or None for wordmarks, href, kind)
LOGOS = [
 ("acx","ACX Grants","https://manifund.org/acx-grants","tile"),
 ("miri",None,"https://intelligence.org/","white"),
 ("far",None,"https://far.ai/","white"),
 ("elicit","Elicit","https://elicit.com/","tile"),
 ("aiimpacts","Impacts","https://aiimpacts.org/","tile"),
 ("rop","Roots of Progress","https://rootsofprogress.org/","tile"),
 ("epoch","Epoch","https://epoch.ai/","tile"),
 ("bluedot",None,"https://bluedot.org/","white"),
 ("lightcone","Lightcone","https://www.lightconeinfrastructure.com/","plain"),
 ("seldon","Seldon","https://seldonlab.com/","tile"),
 ("govai","GovAI","https://governance.ai/","plain"),
 ("arc","ARC","https://www.alignment.org/","plain"),
 ("redwood","Redwood","https://redwoodresearch.org/","plain"),
 ("palisade","Palisade","https://palisaderesearch.org/","plain"),
 ("timaeus","Timaeus","https://timaeus.co/","plain"),
 ("sentient",None,"https://www.sentientfutures.ai/","plain"),
]
OFFICES = [("Gutenberg","Room 201"),("Netholabs","Room 203"),("The Relationship Company","Room 204"),("Neolithic","Room 205"),
 ("Haptica","Room 302"),("Deep AI","Room 302"),("Tampersec","Room 304"),("Confluence","Room 306"),
 ("Chips for Humanity / Hofvarpnir Studios","Room 403"),("hum.ai","Room 404"),("Talarion","Room 406"),("Sentient Futures","Rooms 409, 408"),("Tabula Bio","Room 411"),("Stardrift","Room 412")]
GALLERY = [("024","A crowded open floor during an event"),("002","The lounge with grey sofas"),("026","A reading group around a table on a colorful rug"),("007","Wooden tables by sunny windows"),("021","Members making letters with their bodies in front of the green wall"),("018","Two members and a baby laughing"),("025","A member and a kid playing a game on the floor"),("009","White chairs set up for a talk"),("016","A member working in front of a projected screen")]

def into(a,b):
    if a and b: return f'is into <i>{a}</i> and <i>{b}</i>'
    if a: return f'is into <i>{a}</i>'
    return ''
