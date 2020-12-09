import re

rules1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

rules2 = """clear purple bags contain 5 faded indigo bags, 3 muted purple bags.
bright teal bags contain 4 striped plum bags.
dim fuchsia bags contain 2 vibrant tomato bags, 2 dotted purple bags, 2 plaid indigo bags.
dark magenta bags contain 1 shiny aqua bag, 2 posh white bags.
dark chartreuse bags contain 1 dotted brown bag, 4 vibrant magenta bags.
wavy crimson bags contain 5 pale coral bags.
drab cyan bags contain 1 light green bag, 2 pale teal bags.
posh salmon bags contain 5 wavy maroon bags, 5 shiny coral bags.
light violet bags contain 5 faded teal bags, 1 light gray bag, 4 bright turquoise bags, 5 posh crimson bags.
dark turquoise bags contain 1 clear yellow bag, 1 wavy maroon bag, 3 muted brown bags.
bright coral bags contain 5 mirrored silver bags, 4 light teal bags.
dotted lavender bags contain 1 clear indigo bag.
striped white bags contain 5 dull beige bags.
dotted lime bags contain 5 mirrored magenta bags, 4 faded red bags.
dark tan bags contain 5 bright coral bags, 5 wavy salmon bags, 4 posh green bags.
dull black bags contain 2 shiny brown bags, 3 plaid bronze bags, 3 wavy teal bags, 3 dull chartreuse bags.
wavy coral bags contain 5 clear maroon bags, 3 dotted tan bags.
dotted yellow bags contain 1 shiny green bag, 1 mirrored tomato bag, 5 light bronze bags.
striped tan bags contain 3 pale lime bags.
striped aqua bags contain 5 pale magenta bags, 4 drab magenta bags, 2 dotted violet bags.
drab crimson bags contain 4 posh aqua bags, 4 dim gray bags.
bright indigo bags contain 5 striped violet bags, 1 muted orange bag.
striped yellow bags contain 3 mirrored orange bags, 3 clear black bags, 1 pale magenta bag.
dim teal bags contain 1 drab gold bag.
light green bags contain 4 drab magenta bags, 3 dark orange bags.
posh white bags contain 1 clear teal bag, 3 shiny cyan bags.
wavy fuchsia bags contain 5 vibrant magenta bags, 2 dull maroon bags, 4 faded lime bags.
faded gold bags contain 3 shiny indigo bags, 4 light lime bags.
dotted violet bags contain 4 faded tomato bags, 3 shiny gold bags, 4 faded brown bags, 2 clear bronze bags.
posh olive bags contain 2 pale bronze bags.
mirrored salmon bags contain 3 dim crimson bags, 5 striped plum bags, 5 clear plum bags.
mirrored olive bags contain 4 bright orange bags, 5 dim silver bags, 1 wavy tan bag, 5 striped crimson bags.
shiny orange bags contain 2 dim lime bags, 4 plaid lavender bags, 5 dull indigo bags.
dark fuchsia bags contain 4 dull red bags, 1 dotted fuchsia bag.
wavy white bags contain 5 plaid tomato bags, 5 wavy indigo bags, 5 mirrored brown bags, 3 muted red bags.
plaid violet bags contain 2 faded beige bags, 2 muted gold bags, 4 posh brown bags.
light orange bags contain 2 light tomato bags, 3 clear plum bags.
shiny tan bags contain 5 plaid tan bags, 2 wavy red bags, 1 wavy green bag.
dim gold bags contain 1 dull orange bag.
dark gold bags contain 1 pale cyan bag, 5 dotted beige bags, 3 vibrant teal bags, 1 vibrant magenta bag.
striped tomato bags contain 3 faded white bags, 4 shiny beige bags, 1 bright violet bag, 4 plaid aqua bags.
shiny magenta bags contain 5 dark purple bags, 1 dotted green bag, 2 shiny tomato bags.
plaid tomato bags contain 4 bright coral bags, 1 clear teal bag.
pale turquoise bags contain 3 muted gold bags, 3 dark bronze bags, 5 dotted violet bags, 5 light tomato bags.
shiny silver bags contain 5 pale purple bags, 1 muted maroon bag.
drab brown bags contain 3 dotted yellow bags, 3 wavy maroon bags, 3 striped gold bags, 1 faded aqua bag.
striped olive bags contain 5 bright crimson bags, 5 dim olive bags, 2 pale coral bags, 2 dull orange bags.
plaid gray bags contain 2 dim yellow bags, 5 faded lime bags.
striped violet bags contain 5 shiny gray bags, 1 dim lime bag.
wavy chartreuse bags contain 3 striped magenta bags, 4 muted crimson bags, 5 clear maroon bags.
plaid salmon bags contain 2 bright black bags.
mirrored teal bags contain 1 vibrant crimson bag, 5 plaid magenta bags, 2 muted green bags, 4 wavy brown bags.
drab yellow bags contain 2 posh salmon bags, 3 light purple bags, 3 striped orange bags.
bright purple bags contain 5 muted gold bags, 3 dull olive bags, 5 faded violet bags.
dim magenta bags contain 5 dark olive bags, 2 shiny indigo bags, 5 shiny turquoise bags, 5 dark tan bags.
wavy violet bags contain 5 clear white bags, 5 posh coral bags.
wavy blue bags contain 4 pale chartreuse bags, 2 shiny brown bags.
plaid crimson bags contain 4 faded black bags.
vibrant tomato bags contain 3 posh tomato bags, 2 mirrored silver bags, 5 dotted brown bags.
clear indigo bags contain 1 wavy indigo bag.
mirrored fuchsia bags contain 2 vibrant coral bags, 5 clear tan bags, 2 pale indigo bags, 1 drab bronze bag.
light silver bags contain 5 pale plum bags, 5 clear black bags, 1 pale red bag.
dim tan bags contain 1 pale plum bag.
pale salmon bags contain 4 dim lime bags.
light lime bags contain 1 bright fuchsia bag, 1 bright olive bag.
dim red bags contain 5 clear silver bags.
striped chartreuse bags contain 5 dim chartreuse bags, 3 pale cyan bags.
bright gray bags contain 2 posh teal bags, 1 dark turquoise bag, 4 light yellow bags.
wavy gold bags contain 5 drab white bags, 2 wavy salmon bags, 5 dim lime bags, 4 plaid tomato bags.
pale maroon bags contain 3 vibrant magenta bags, 5 dim maroon bags, 4 dull aqua bags, 5 bright coral bags.
shiny aqua bags contain 5 dotted brown bags.
dark tomato bags contain 5 dull violet bags, 1 vibrant magenta bag, 3 muted brown bags.
faded aqua bags contain 1 bright fuchsia bag, 5 dotted violet bags, 4 shiny gold bags.
dark plum bags contain 5 dull aqua bags, 3 faded red bags.
plaid aqua bags contain 3 drab gold bags, 3 faded tomato bags, 5 plaid cyan bags.
faded teal bags contain 1 vibrant beige bag, 5 posh crimson bags.
muted coral bags contain 1 dim plum bag, 1 wavy salmon bag, 5 plaid cyan bags.
posh gray bags contain 3 posh tomato bags.
plaid black bags contain 4 faded aqua bags.
wavy gray bags contain 1 shiny blue bag.
shiny maroon bags contain 2 wavy crimson bags, 1 dotted coral bag, 3 bright tan bags.
mirrored lime bags contain 5 plaid purple bags.
dotted chartreuse bags contain 5 light salmon bags.
vibrant gold bags contain 5 plaid purple bags, 3 bright olive bags, 5 vibrant yellow bags.
wavy yellow bags contain 3 light tomato bags.
drab violet bags contain 2 light violet bags, 1 vibrant tomato bag, 3 dim bronze bags, 5 striped lavender bags.
pale lime bags contain 3 striped blue bags, 3 shiny indigo bags, 5 posh gold bags.
light lavender bags contain 2 faded chartreuse bags, 3 dim lime bags, 4 faded brown bags.
mirrored chartreuse bags contain 5 dotted violet bags, 2 faded brown bags.
clear beige bags contain 4 faded violet bags, 3 clear white bags, 5 plaid indigo bags, 2 wavy indigo bags.
dull lime bags contain 4 plaid black bags, 5 pale bronze bags, 1 bright plum bag.
muted violet bags contain 4 drab white bags, 4 muted silver bags, 4 dotted bronze bags.
faded white bags contain 4 plaid olive bags.
striped teal bags contain 2 drab crimson bags, 3 clear maroon bags, 4 muted blue bags, 2 posh green bags.
dull teal bags contain 5 wavy yellow bags.
wavy maroon bags contain 2 mirrored salmon bags, 2 light teal bags, 5 posh gray bags, 3 muted olive bags.
vibrant salmon bags contain 3 light turquoise bags, 4 striped maroon bags, 3 mirrored white bags, 2 bright olive bags.
striped green bags contain 5 faded gray bags, 2 pale green bags, 4 posh blue bags.
posh tan bags contain 4 clear salmon bags.
wavy green bags contain 1 vibrant plum bag, 1 muted crimson bag, 4 light teal bags, 2 mirrored salmon bags.
dotted white bags contain 3 plaid teal bags, 1 shiny indigo bag.
muted tomato bags contain 4 pale gray bags, 5 wavy red bags, 5 dark violet bags, 3 posh aqua bags.
drab beige bags contain 5 wavy aqua bags.
pale purple bags contain 4 striped black bags, 1 light turquoise bag.
muted indigo bags contain 5 dim gold bags, 2 dull turquoise bags, 4 dotted olive bags.
pale coral bags contain 2 vibrant beige bags.
dark beige bags contain 5 pale turquoise bags.
posh crimson bags contain 5 dark aqua bags, 3 posh teal bags, 5 dull aqua bags.
dim purple bags contain 5 drab crimson bags, 3 pale aqua bags, 5 clear orange bags.
shiny teal bags contain 4 shiny tan bags, 2 striped salmon bags, 5 drab lime bags.
muted crimson bags contain no other bags.
plaid green bags contain 3 pale bronze bags.
dim aqua bags contain 2 light lime bags, 4 posh green bags, 5 clear white bags.
plaid lavender bags contain 2 striped lime bags.
dark olive bags contain 1 drab magenta bag, 1 bright magenta bag, 2 plaid crimson bags.
striped crimson bags contain 2 vibrant white bags, 1 pale bronze bag, 2 striped blue bags, 4 pale coral bags.
striped lime bags contain 3 shiny gold bags, 1 muted coral bag, 3 dotted red bags.
plaid silver bags contain 2 drab aqua bags, 2 striped orange bags, 2 plaid crimson bags.
dotted tan bags contain 3 light purple bags, 1 clear teal bag, 5 dotted crimson bags, 2 dim lime bags.
clear blue bags contain 5 dotted green bags, 5 drab crimson bags, 2 wavy tomato bags.
muted green bags contain 3 clear maroon bags, 5 dull orange bags.
dull blue bags contain 3 light silver bags.
striped purple bags contain 4 vibrant tomato bags, 1 dark bronze bag, 1 mirrored white bag.
light salmon bags contain 3 muted coral bags, 1 mirrored yellow bag, 4 faded red bags, 3 muted silver bags.
wavy black bags contain 5 clear indigo bags, 4 dotted purple bags, 3 posh violet bags, 4 bright magenta bags.
mirrored crimson bags contain 3 muted gray bags, 5 drab chartreuse bags.
vibrant bronze bags contain 1 mirrored turquoise bag, 3 dull crimson bags, 3 faded purple bags, 5 dotted beige bags.
pale teal bags contain 5 clear green bags.
muted red bags contain 3 dim plum bags, 3 clear bronze bags.
mirrored aqua bags contain 2 posh aqua bags, 1 plaid tomato bag, 1 mirrored magenta bag, 4 dim chartreuse bags.
dim yellow bags contain 5 bright fuchsia bags, 5 drab tan bags, 1 dark blue bag.
vibrant green bags contain 3 dull aqua bags, 2 posh cyan bags.
mirrored black bags contain 2 striped gray bags.
striped turquoise bags contain 1 shiny gold bag, 4 shiny turquoise bags.
wavy plum bags contain 4 pale brown bags, 4 dark plum bags, 1 bright lavender bag.
dotted purple bags contain 2 dim maroon bags.
posh teal bags contain 1 clear plum bag, 4 faded black bags, 1 dim crimson bag.
shiny crimson bags contain 1 faded red bag.
mirrored beige bags contain 1 faded bronze bag.
dotted olive bags contain 5 pale plum bags, 4 muted plum bags.
bright lime bags contain 3 faded beige bags, 3 wavy fuchsia bags, 3 vibrant plum bags, 3 shiny coral bags.
pale bronze bags contain 5 faded crimson bags, 4 vibrant tan bags, 2 pale coral bags.
dim coral bags contain 5 drab maroon bags, 4 striped violet bags, 1 plaid crimson bag, 2 dim white bags.
bright violet bags contain 5 clear white bags, 1 plaid beige bag.
plaid gold bags contain 2 striped maroon bags.
dull red bags contain 4 wavy tomato bags, 5 clear beige bags.
muted tan bags contain 3 pale beige bags, 4 dotted beige bags, 5 dull cyan bags, 1 striped gold bag.
posh plum bags contain 3 vibrant purple bags, 2 light tomato bags, 3 drab maroon bags, 3 plaid tomato bags.
dotted gold bags contain 1 posh violet bag, 4 dim purple bags, 3 shiny tomato bags.
posh black bags contain 1 muted olive bag, 5 striped turquoise bags, 1 wavy crimson bag.
shiny beige bags contain 2 dull teal bags, 3 striped lavender bags, 3 vibrant indigo bags, 3 mirrored magenta bags.
posh silver bags contain 1 wavy black bag.
dotted bronze bags contain 3 dim plum bags, 1 posh gray bag, 5 mirrored crimson bags, 5 mirrored lime bags.
pale indigo bags contain 2 wavy black bags, 4 shiny aqua bags, 1 striped lime bag.
muted olive bags contain 4 faded brown bags, 1 muted gold bag, 1 faded teal bag, 2 vibrant orange bags.
shiny white bags contain 2 wavy purple bags.
bright yellow bags contain 5 dotted gray bags, 5 clear indigo bags, 2 clear turquoise bags.
pale tan bags contain 5 dotted purple bags, 1 vibrant white bag, 3 pale red bags, 3 mirrored yellow bags.
drab gray bags contain 5 dotted maroon bags, 3 shiny fuchsia bags, 5 dim lime bags, 3 mirrored brown bags.
drab blue bags contain 4 striped purple bags, 3 plaid tomato bags.
posh indigo bags contain 3 muted blue bags.
dotted turquoise bags contain 1 vibrant plum bag, 5 clear gray bags, 2 wavy yellow bags.
light red bags contain 2 muted silver bags, 5 drab chartreuse bags, 4 wavy cyan bags.
drab red bags contain 3 dotted tomato bags, 3 dotted plum bags, 5 drab orange bags, 4 wavy teal bags.
dotted beige bags contain 5 light violet bags.
clear gray bags contain 3 shiny gold bags, 3 dull orange bags, 5 light fuchsia bags, 5 vibrant beige bags.
vibrant beige bags contain 2 drab magenta bags, 5 dim maroon bags, 3 bright turquoise bags, 3 dim plum bags.
dark brown bags contain 2 striped cyan bags, 5 vibrant yellow bags.
bright blue bags contain 4 vibrant lime bags, 4 faded yellow bags, 1 clear orange bag, 4 wavy gray bags.
dull plum bags contain 3 mirrored salmon bags.
striped gold bags contain 1 faded teal bag, 4 vibrant plum bags.
dotted gray bags contain 1 faded black bag, 1 pale tomato bag.
plaid olive bags contain 2 clear gray bags, 5 dotted tan bags.
faded plum bags contain 4 light turquoise bags, 1 dim brown bag, 3 shiny turquoise bags, 1 posh chartreuse bag.
clear turquoise bags contain 2 bright coral bags, 3 drab cyan bags.
wavy brown bags contain 5 clear yellow bags, 5 dim silver bags, 1 mirrored white bag.
muted maroon bags contain 3 posh aqua bags, 2 drab yellow bags, 3 pale crimson bags, 1 dotted maroon bag.
clear plum bags contain no other bags.
dim silver bags contain 1 bright fuchsia bag.
dotted silver bags contain 2 dotted indigo bags, 2 faded chartreuse bags, 3 wavy white bags.
vibrant olive bags contain 3 posh coral bags, 3 drab aqua bags.
faded yellow bags contain 1 plaid tomato bag, 1 light tomato bag.
drab lavender bags contain 3 light gray bags, 3 dotted beige bags, 4 dull tomato bags.
drab tomato bags contain 4 wavy aqua bags, 1 posh teal bag, 5 clear red bags, 4 clear plum bags.
pale beige bags contain 5 wavy salmon bags.
pale magenta bags contain 5 bright fuchsia bags.
dotted black bags contain 3 mirrored lime bags.
bright plum bags contain 5 vibrant teal bags.
bright lavender bags contain 5 dotted purple bags, 1 faded black bag, 4 light purple bags.
muted yellow bags contain 4 dotted aqua bags, 1 dim cyan bag.
shiny tomato bags contain 1 dim crimson bag.
dotted magenta bags contain 2 clear maroon bags, 5 plaid gold bags.
dull aqua bags contain 2 shiny blue bags.
faded silver bags contain 4 faded brown bags, 1 muted brown bag.
muted gray bags contain 2 light yellow bags, 5 mirrored brown bags, 3 bright teal bags, 5 posh teal bags.
mirrored gold bags contain 4 shiny black bags, 5 shiny coral bags, 2 clear orange bags, 4 mirrored aqua bags.
plaid teal bags contain 4 dull orange bags, 2 shiny gold bags, 2 plaid crimson bags, 4 clear green bags.
light white bags contain 5 vibrant white bags, 1 posh lavender bag, 3 clear white bags.
shiny turquoise bags contain 3 bright turquoise bags.
muted orange bags contain 1 bright tan bag, 1 shiny teal bag, 5 bright gold bags.
mirrored bronze bags contain 2 drab white bags, 4 clear bronze bags, 3 drab blue bags.
shiny green bags contain 4 mirrored cyan bags.
posh tomato bags contain 3 dull orange bags, 2 clear plum bags.
shiny salmon bags contain 2 vibrant tomato bags, 3 muted olive bags, 2 dim bronze bags.
muted purple bags contain 4 shiny turquoise bags.
dim lime bags contain 3 posh teal bags.
muted chartreuse bags contain 1 dotted fuchsia bag, 4 light teal bags, 4 dull salmon bags.
mirrored yellow bags contain 4 wavy brown bags.
drab teal bags contain 1 mirrored maroon bag, 1 faded fuchsia bag, 3 bright coral bags, 2 dull purple bags.
plaid plum bags contain 4 dark cyan bags.
dim indigo bags contain 3 dotted gold bags, 5 muted coral bags, 2 posh plum bags.
wavy aqua bags contain 4 drab gold bags, 5 wavy yellow bags.
vibrant brown bags contain 3 posh violet bags, 4 pale magenta bags.
faded maroon bags contain 4 dull maroon bags, 4 light indigo bags, 4 wavy beige bags, 1 clear olive bag.
light crimson bags contain 1 dim gray bag.
plaid orange bags contain 5 plaid bronze bags, 1 dark orange bag.
clear gold bags contain 5 plaid black bags, 4 faded coral bags.
mirrored gray bags contain 1 shiny coral bag, 3 pale beige bags, 1 dark tan bag.
dark gray bags contain 4 dim turquoise bags, 3 clear gray bags.
light fuchsia bags contain 3 dotted brown bags, 3 clear maroon bags.
posh cyan bags contain 2 dotted violet bags.
light cyan bags contain 2 drab maroon bags, 5 vibrant indigo bags, 3 dull tomato bags, 3 wavy gray bags.
wavy olive bags contain 5 wavy cyan bags, 4 mirrored tomato bags.
faded indigo bags contain 4 bright bronze bags, 5 dim lime bags.
muted plum bags contain 1 clear maroon bag.
muted brown bags contain 2 posh gray bags.
pale tomato bags contain 3 dull cyan bags, 3 faded beige bags.
striped blue bags contain 1 faded tomato bag, 3 dotted purple bags.
dotted fuchsia bags contain 2 posh green bags, 1 faded aqua bag.
vibrant fuchsia bags contain 3 mirrored white bags.
pale cyan bags contain 3 dotted green bags, 3 drab maroon bags.
wavy silver bags contain 1 vibrant yellow bag, 5 mirrored chartreuse bags, 1 drab magenta bag, 2 faded tan bags.
vibrant black bags contain 3 dotted purple bags, 3 bright coral bags.
dull bronze bags contain 5 dull white bags, 4 dark olive bags.
wavy purple bags contain 2 dim lavender bags, 5 striped red bags, 4 posh yellow bags, 1 dotted fuchsia bag.
dim salmon bags contain 3 vibrant magenta bags, 4 wavy fuchsia bags, 1 plaid fuchsia bag, 2 dim magenta bags.
dim orange bags contain 2 muted lime bags.
plaid fuchsia bags contain 1 vibrant crimson bag, 1 dotted beige bag, 5 wavy gray bags, 1 dim bronze bag.
dark black bags contain 2 posh lavender bags, 4 light black bags, 5 bright orange bags.
muted teal bags contain 5 clear red bags, 4 vibrant magenta bags, 1 vibrant aqua bag.
mirrored lavender bags contain 1 faded bronze bag, 2 bright violet bags, 4 dull turquoise bags.
dark lavender bags contain 5 dotted gold bags, 2 dark turquoise bags, 1 dark brown bag.
dull brown bags contain 2 faded brown bags, 3 dotted lime bags, 5 dull plum bags, 3 dull white bags.
pale gray bags contain 1 pale salmon bag, 5 dotted fuchsia bags.
light coral bags contain 2 bright magenta bags, 1 wavy brown bag.
dull tan bags contain 5 shiny turquoise bags, 5 light cyan bags, 2 faded indigo bags.
dim bronze bags contain 5 striped blue bags.
bright tomato bags contain 1 striped black bag.
shiny chartreuse bags contain 4 plaid aqua bags, 1 striped tomato bag, 3 striped black bags, 4 dull maroon bags.
mirrored silver bags contain 4 shiny blue bags, 4 dotted maroon bags, 3 clear maroon bags, 4 clear plum bags.
pale olive bags contain 5 drab brown bags, 1 bright lime bag, 1 vibrant lime bag, 3 muted blue bags.
pale gold bags contain 1 mirrored chartreuse bag, 4 posh silver bags.
plaid indigo bags contain 1 bright fuchsia bag, 1 wavy indigo bag, 5 dark aqua bags.
mirrored green bags contain 4 mirrored crimson bags, 2 dull turquoise bags.
shiny fuchsia bags contain 4 wavy crimson bags.
drab salmon bags contain 1 faded silver bag, 4 muted white bags, 4 clear yellow bags.
bright salmon bags contain 4 bright crimson bags, 1 muted tomato bag.
posh chartreuse bags contain 3 posh cyan bags, 4 plaid cyan bags.
wavy cyan bags contain 1 vibrant magenta bag, 2 posh crimson bags.
shiny indigo bags contain 1 plaid teal bag.
shiny purple bags contain 1 dark purple bag, 5 dull magenta bags, 3 plaid fuchsia bags.
bright gold bags contain 3 faded aqua bags.
vibrant yellow bags contain 3 vibrant brown bags, 3 wavy green bags, 5 dotted brown bags, 5 striped plum bags.
muted beige bags contain 4 vibrant tomato bags, 3 dull fuchsia bags.
dim maroon bags contain no other bags.
mirrored tan bags contain 3 pale turquoise bags, 3 muted olive bags, 3 shiny violet bags.
striped gray bags contain 5 mirrored gold bags.
drab purple bags contain 1 wavy orange bag.
dull silver bags contain 4 clear chartreuse bags, 4 posh cyan bags, 2 pale salmon bags, 3 shiny lavender bags.
dim blue bags contain 1 clear turquoise bag, 1 clear orange bag, 4 clear teal bags.
dull maroon bags contain 2 striped plum bags.
posh magenta bags contain 4 dim gray bags.
light beige bags contain 4 dotted turquoise bags, 1 pale cyan bag.
dim olive bags contain 3 plaid teal bags, 5 faded brown bags, 1 faded crimson bag.
light tomato bags contain no other bags.
drab black bags contain 2 wavy brown bags, 1 dull maroon bag, 5 muted crimson bags, 3 posh green bags.
posh coral bags contain 1 drab gray bag, 1 striped red bag.
mirrored cyan bags contain 4 drab gray bags.
dotted salmon bags contain 4 striped coral bags, 2 muted purple bags.
bright maroon bags contain 1 faded crimson bag, 4 clear maroon bags, 2 faded brown bags.
light turquoise bags contain 2 shiny lime bags, 5 dotted violet bags, 3 vibrant tan bags, 5 shiny cyan bags.
faded black bags contain 4 drab magenta bags, 3 dim plum bags, 5 bright fuchsia bags.
vibrant silver bags contain 2 clear violet bags, 2 drab orange bags, 5 plaid magenta bags, 5 shiny violet bags.
vibrant tan bags contain 3 clear bronze bags, 5 vibrant tomato bags, 4 light teal bags.
clear bronze bags contain 1 posh green bag, 4 faded brown bags, 1 shiny violet bag.
striped salmon bags contain 2 dark fuchsia bags, 4 shiny chartreuse bags.
wavy indigo bags contain no other bags.
dark violet bags contain 5 dull violet bags, 3 wavy tomato bags, 5 pale green bags.
drab magenta bags contain 4 wavy indigo bags, 2 dark aqua bags, 4 dotted brown bags, 2 muted crimson bags.
dark orange bags contain 3 faded violet bags, 3 shiny coral bags, 4 light violet bags.
drab green bags contain 1 light tan bag, 2 plaid tomato bags.
mirrored magenta bags contain 4 vibrant plum bags, 4 vibrant black bags.
muted cyan bags contain 1 dull aqua bag, 3 dark cyan bags.
dim plum bags contain 2 wavy yellow bags, 3 bright fuchsia bags.
dark bronze bags contain 2 shiny violet bags, 2 clear plum bags.
striped coral bags contain 3 shiny coral bags.
faded violet bags contain 4 plaid indigo bags.
posh brown bags contain 5 posh magenta bags, 5 bright fuchsia bags, 1 vibrant plum bag.
drab coral bags contain 5 vibrant beige bags.
plaid tan bags contain 5 dark orange bags, 5 dotted tan bags.
dark silver bags contain 1 pale plum bag, 5 bright cyan bags, 3 wavy aqua bags.
dark lime bags contain 3 drab green bags, 5 light crimson bags.
dull salmon bags contain 3 dull maroon bags, 5 striped gold bags, 2 dotted maroon bags.
bright white bags contain 5 pale teal bags, 2 posh white bags, 2 bright crimson bags, 3 pale fuchsia bags.
vibrant violet bags contain 5 dim brown bags, 2 bright brown bags, 2 pale coral bags, 1 wavy plum bag.
vibrant magenta bags contain 2 clear maroon bags, 3 wavy indigo bags, 5 plaid bronze bags.
faded coral bags contain 5 vibrant maroon bags, 3 mirrored beige bags.
dark teal bags contain 1 dark tan bag, 2 posh chartreuse bags.
dark crimson bags contain 2 dark fuchsia bags, 5 striped blue bags.
dull yellow bags contain 1 faded bronze bag, 4 dark beige bags, 5 plaid black bags, 1 posh salmon bag.
plaid magenta bags contain 1 plaid beige bag, 2 posh teal bags.
pale chartreuse bags contain 1 plaid orange bag, 2 vibrant beige bags, 5 muted gold bags.
posh lavender bags contain 3 plaid violet bags, 4 dark blue bags, 2 wavy teal bags, 5 vibrant black bags.
dull purple bags contain 2 posh lime bags, 1 wavy olive bag, 1 striped red bag, 5 pale lime bags.
bright tan bags contain 2 shiny tan bags, 4 clear green bags, 1 light violet bag.
pale plum bags contain 4 dull crimson bags, 2 vibrant orange bags, 2 striped cyan bags.
clear crimson bags contain 3 mirrored silver bags.
light blue bags contain 5 dull magenta bags, 4 clear black bags, 2 bright tan bags, 1 dotted teal bag.
muted turquoise bags contain 3 bright red bags, 3 light tomato bags, 3 dull gold bags, 4 clear cyan bags.
muted lime bags contain 5 dim olive bags, 3 pale fuchsia bags.
clear green bags contain 5 dim maroon bags, 4 bright fuchsia bags, 1 muted crimson bag, 1 shiny blue bag.
dim green bags contain 2 pale turquoise bags.
plaid red bags contain 3 plaid silver bags.
mirrored brown bags contain 1 clear plum bag.
dull lavender bags contain 1 clear teal bag.
shiny brown bags contain 5 shiny coral bags, 1 posh black bag, 2 dotted maroon bags, 2 muted olive bags.
dotted green bags contain 2 clear crimson bags, 2 dim gray bags, 1 plaid green bag, 1 dotted maroon bag.
vibrant maroon bags contain 2 mirrored brown bags, 5 shiny coral bags.
dotted tomato bags contain 3 wavy coral bags, 3 dotted crimson bags.
vibrant turquoise bags contain 5 posh tomato bags, 2 faded bronze bags.
bright aqua bags contain 4 light tan bags.
clear teal bags contain 1 mirrored salmon bag, 4 dark aqua bags.
shiny gray bags contain 3 mirrored crimson bags, 4 drab chartreuse bags.
muted black bags contain 4 wavy orange bags.
posh yellow bags contain 4 plaid teal bags.
pale black bags contain 5 wavy brown bags, 1 mirrored yellow bag.
dark red bags contain 5 striped magenta bags, 5 plaid salmon bags.
dull magenta bags contain 2 light white bags, 3 mirrored blue bags, 3 faded black bags, 5 shiny coral bags.
mirrored orange bags contain 5 posh white bags.
dark salmon bags contain 2 posh fuchsia bags.
bright brown bags contain 4 posh blue bags, 3 shiny brown bags.
drab lime bags contain 4 dotted maroon bags, 3 pale bronze bags, 2 striped black bags.
dull violet bags contain 5 bright lavender bags, 1 shiny coral bag.
muted silver bags contain 1 muted coral bag.
dull olive bags contain 4 pale cyan bags, 5 drab green bags, 4 clear turquoise bags.
light aqua bags contain 4 posh orange bags, 4 dull fuchsia bags.
vibrant coral bags contain 1 clear bronze bag, 3 striped brown bags.
muted magenta bags contain 1 clear fuchsia bag, 5 shiny crimson bags, 4 shiny gold bags, 2 plaid cyan bags.
faded blue bags contain 5 plaid green bags.
clear cyan bags contain 3 drab cyan bags.
wavy beige bags contain 4 mirrored white bags, 4 bright white bags, 5 dark beige bags, 5 pale tomato bags.
light maroon bags contain 3 vibrant maroon bags, 1 dark orange bag, 3 drab plum bags.
faded green bags contain 1 vibrant black bag.
vibrant teal bags contain 4 shiny violet bags.
clear coral bags contain 4 dark maroon bags, 1 striped tomato bag, 4 light orange bags.
pale lavender bags contain 4 light green bags, 2 drab magenta bags.
muted blue bags contain 5 pale cyan bags, 4 posh teal bags.
mirrored plum bags contain 5 drab aqua bags, 3 striped gold bags.
dull chartreuse bags contain 1 dull orange bag, 5 clear chartreuse bags.
faded magenta bags contain 4 bright blue bags.
dim cyan bags contain 1 muted brown bag, 3 posh magenta bags.
dim beige bags contain 3 shiny blue bags, 4 dim black bags.
faded tomato bags contain 1 vibrant magenta bag, 2 plaid cyan bags, 4 muted crimson bags.
clear aqua bags contain 1 dull bronze bag, 4 shiny bronze bags.
pale fuchsia bags contain 2 mirrored orange bags.
drab olive bags contain 3 wavy salmon bags.
clear white bags contain 1 vibrant teal bag, 1 posh tomato bag, 5 vibrant aqua bags.
drab orange bags contain 3 striped gold bags, 2 mirrored tan bags, 3 dull tomato bags, 2 wavy aqua bags.
plaid purple bags contain 3 dotted maroon bags, 5 shiny turquoise bags.
mirrored violet bags contain 4 clear white bags, 2 shiny black bags.
dotted teal bags contain 2 dim teal bags, 1 striped fuchsia bag.
bright beige bags contain 2 dim silver bags, 3 dull beige bags.
dim turquoise bags contain 1 plaid silver bag, 1 light yellow bag, 2 shiny orange bags, 3 striped cyan bags.
dotted brown bags contain no other bags.
drab maroon bags contain 4 clear plum bags, 4 shiny coral bags.
dark indigo bags contain 1 mirrored magenta bag.
posh bronze bags contain 3 bright bronze bags, 4 dotted maroon bags, 3 wavy tomato bags, 4 dotted lime bags.
vibrant cyan bags contain 5 wavy brown bags.
drab turquoise bags contain 2 muted silver bags, 2 bright maroon bags, 5 dim gray bags.
pale red bags contain 1 shiny coral bag, 5 mirrored silver bags, 3 shiny turquoise bags.
vibrant lime bags contain 4 light lavender bags, 4 mirrored tomato bags.
dim black bags contain 2 light beige bags, 1 plaid cyan bag, 2 posh yellow bags, 3 vibrant cyan bags.
dull coral bags contain 5 dull orange bags, 1 dotted green bag.
posh violet bags contain 5 light green bags, 3 pale teal bags.
bright silver bags contain 5 wavy white bags, 2 vibrant salmon bags.
light plum bags contain 4 light indigo bags, 1 posh gold bag.
plaid coral bags contain 4 dark olive bags.
bright magenta bags contain 1 bright fuchsia bag, 4 dim crimson bags, 2 clear yellow bags, 2 bright lavender bags.
striped lavender bags contain 4 dull orange bags.
drab aqua bags contain 4 vibrant tan bags, 3 vibrant crimson bags, 1 dotted purple bag.
shiny blue bags contain 2 plaid bronze bags.
wavy lime bags contain 2 drab orange bags.
dull white bags contain 4 light teal bags.
pale orange bags contain 2 plaid yellow bags, 1 posh indigo bag.
faded chartreuse bags contain 4 dull tomato bags, 3 mirrored salmon bags.
bright orange bags contain 4 vibrant yellow bags, 4 vibrant salmon bags, 3 faded white bags, 4 clear orange bags.
dark blue bags contain 3 vibrant indigo bags.
striped indigo bags contain 3 vibrant magenta bags.
mirrored blue bags contain 5 bright crimson bags, 5 light salmon bags, 5 dark olive bags.
plaid chartreuse bags contain 5 drab tomato bags, 1 dark tan bag, 4 dotted crimson bags, 5 dark bronze bags.
shiny cyan bags contain 1 shiny aqua bag, 5 clear plum bags, 1 posh gray bag, 5 shiny coral bags.
dim violet bags contain 3 drab chartreuse bags, 4 pale lavender bags, 5 shiny gold bags.
dotted orange bags contain 5 plaid chartreuse bags, 4 vibrant purple bags, 5 posh teal bags.
clear magenta bags contain 3 clear indigo bags.
vibrant chartreuse bags contain 4 faded violet bags.
dark cyan bags contain 2 dim plum bags, 5 light purple bags, 1 dark olive bag, 2 dim maroon bags.
light olive bags contain 5 pale lime bags, 2 mirrored lime bags.
vibrant lavender bags contain 2 pale black bags.
plaid maroon bags contain 4 clear white bags.
pale aqua bags contain 2 shiny tomato bags, 4 dim gold bags, 5 pale green bags.
posh blue bags contain 1 wavy fuchsia bag, 3 light cyan bags, 1 striped beige bag.
clear lime bags contain 4 mirrored gold bags, 2 wavy coral bags.
pale yellow bags contain 2 dull cyan bags, 1 dotted maroon bag, 3 light teal bags, 1 clear gray bag.
muted lavender bags contain 1 wavy cyan bag.
light magenta bags contain 5 shiny lime bags, 3 light indigo bags, 2 clear beige bags.
dotted maroon bags contain 4 wavy yellow bags, 5 bright fuchsia bags, 5 faded brown bags.
shiny red bags contain 2 faded tomato bags, 3 faded black bags, 2 pale teal bags, 5 muted bronze bags.
shiny lavender bags contain 1 bright yellow bag, 2 plaid purple bags, 2 light coral bags, 4 pale purple bags.
clear violet bags contain 1 plaid chartreuse bag.
muted white bags contain 1 striped turquoise bag.
plaid bronze bags contain no other bags.
faded fuchsia bags contain 5 clear red bags.
dull orange bags contain 5 drab gold bags, 2 dotted purple bags, 4 bright turquoise bags, 4 plaid bronze bags.
clear red bags contain 4 clear crimson bags, 3 bright turquoise bags, 3 clear green bags.
vibrant aqua bags contain 5 light gray bags, 3 light tomato bags, 5 vibrant white bags, 5 posh tomato bags.
drab bronze bags contain 3 striped fuchsia bags, 3 vibrant coral bags, 3 posh turquoise bags, 5 clear maroon bags.
dotted crimson bags contain 4 muted teal bags, 5 dull violet bags, 2 muted gold bags.
mirrored purple bags contain 5 drab black bags, 1 dotted teal bag.
dark aqua bags contain no other bags.
light tan bags contain 5 dotted tan bags.
wavy turquoise bags contain 2 mirrored cyan bags, 4 mirrored magenta bags, 5 dull salmon bags, 2 vibrant tomato bags.
light black bags contain 5 clear plum bags, 5 faded olive bags.
vibrant blue bags contain 4 dark crimson bags, 2 clear indigo bags, 2 pale lime bags.
clear silver bags contain 1 striped coral bag, 5 faded crimson bags, 5 mirrored chartreuse bags, 2 vibrant magenta bags.
shiny gold bags contain 5 plaid bronze bags, 4 bright fuchsia bags, 2 light violet bags, 1 clear plum bag.
bright red bags contain 2 pale coral bags.
dull tomato bags contain 3 mirrored salmon bags.
clear fuchsia bags contain 3 bright brown bags.
faded orange bags contain 4 clear plum bags, 5 faded maroon bags.
clear black bags contain 2 plaid aqua bags, 2 faded yellow bags, 2 bright magenta bags, 5 striped blue bags.
drab white bags contain 1 muted olive bag, 5 posh magenta bags, 3 plaid tan bags.
wavy salmon bags contain 1 clear maroon bag.
shiny yellow bags contain 2 bright magenta bags.
shiny lime bags contain 4 shiny turquoise bags, 2 mirrored white bags, 4 faded bronze bags, 1 vibrant white bag.
clear yellow bags contain 5 shiny violet bags, 4 light tomato bags, 3 clear plum bags, 1 wavy indigo bag.
wavy red bags contain 2 dim crimson bags, 5 plaid cyan bags.
dotted red bags contain 5 dim plum bags.
faded red bags contain 3 striped maroon bags.
muted gold bags contain 1 vibrant teal bag, 3 faded crimson bags.
dotted aqua bags contain 2 dotted coral bags, 4 faded maroon bags.
vibrant purple bags contain 3 posh aqua bags, 2 light gray bags.
faded salmon bags contain 5 plaid brown bags, 4 drab white bags, 5 wavy olive bags.
light chartreuse bags contain 4 shiny coral bags, 2 shiny purple bags.
dim brown bags contain 5 clear bronze bags, 2 striped orange bags, 5 dark olive bags.
striped black bags contain 1 dark orange bag, 4 faded red bags.
dark white bags contain 5 clear white bags, 2 dull bronze bags, 5 dull chartreuse bags, 3 dark crimson bags.
striped brown bags contain 1 shiny indigo bag, 1 vibrant black bag.
bright olive bags contain 4 striped black bags, 3 dull violet bags, 3 vibrant orange bags.
dull green bags contain 4 dotted orange bags, 5 dotted coral bags, 5 pale tan bags, 1 faded beige bag.
faded bronze bags contain 3 shiny blue bags.
faded tan bags contain 2 pale bronze bags.
plaid cyan bags contain 4 clear maroon bags, 5 dark aqua bags, 1 bright fuchsia bag, 2 plaid bronze bags.
striped bronze bags contain 1 vibrant silver bag, 1 dim red bag, 3 vibrant maroon bags.
dotted blue bags contain 2 vibrant tan bags.
drab gold bags contain 2 dim crimson bags, 3 faded tomato bags, 2 drab magenta bags.
faded cyan bags contain 3 dotted lavender bags, 4 mirrored plum bags, 2 plaid olive bags, 1 muted lime bag.
dark green bags contain 5 dim crimson bags, 4 vibrant aqua bags, 1 pale beige bag, 5 faded aqua bags.
posh green bags contain 4 dim maroon bags, 3 faded black bags, 5 wavy yellow bags.
pale brown bags contain 3 dull coral bags.
light yellow bags contain 5 vibrant black bags.
mirrored coral bags contain 1 wavy teal bag, 5 plaid gold bags, 4 muted crimson bags, 3 clear teal bags.
plaid blue bags contain 2 vibrant tomato bags, 3 light fuchsia bags, 1 shiny tomato bag, 1 faded red bag.
light gold bags contain 1 plaid chartreuse bag, 3 plaid tan bags.
light brown bags contain 4 light green bags, 1 shiny orange bag.
light gray bags contain 3 drab magenta bags.
wavy teal bags contain 2 drab tan bags.
drab tan bags contain 5 light tomato bags, 3 muted tan bags, 3 shiny blue bags, 1 dull white bag.
plaid beige bags contain 5 muted crimson bags, 5 faded white bags, 5 dull aqua bags.
striped fuchsia bags contain 5 dim plum bags, 1 faded gray bag, 2 pale turquoise bags, 3 dull teal bags.
vibrant red bags contain 3 dim aqua bags, 5 plaid green bags.
faded crimson bags contain 3 faded brown bags.
muted aqua bags contain 5 muted purple bags, 5 drab tan bags, 2 shiny magenta bags.
pale blue bags contain 4 pale lavender bags.
wavy tomato bags contain 2 striped plum bags, 4 dull aqua bags, 3 light tan bags, 4 pale black bags.
drab fuchsia bags contain 2 muted purple bags, 2 striped lime bags, 4 clear white bags, 1 bright turquoise bag.
dim crimson bags contain 3 light tomato bags, 5 muted crimson bags, 4 plaid bronze bags, 2 faded tomato bags.
faded turquoise bags contain 5 posh yellow bags, 3 plaid chartreuse bags.
vibrant indigo bags contain 5 bright turquoise bags.
mirrored turquoise bags contain 4 light lavender bags, 2 wavy turquoise bags, 2 wavy red bags.
posh turquoise bags contain 4 posh crimson bags.
vibrant white bags contain 2 dotted purple bags, 5 faded teal bags, 4 faded tomato bags, 5 dull aqua bags.
faded olive bags contain 4 bright bronze bags, 2 vibrant purple bags, 3 dotted violet bags.
posh orange bags contain 4 light green bags, 5 vibrant white bags, 1 shiny lime bag.
pale violet bags contain 3 drab indigo bags.
dotted indigo bags contain 5 bright coral bags, 3 plaid purple bags.
clear tan bags contain 4 dim plum bags, 5 vibrant purple bags.
vibrant orange bags contain 3 striped plum bags.
shiny violet bags contain 5 plaid cyan bags, 5 striped plum bags.
striped silver bags contain 1 clear yellow bag, 3 dotted green bags.
bright chartreuse bags contain 5 wavy tomato bags, 2 bright yellow bags.
vibrant plum bags contain 3 wavy yellow bags, 5 dim maroon bags, 5 plaid bronze bags.
clear maroon bags contain no other bags.
wavy orange bags contain 3 plaid aqua bags, 1 pale salmon bag.
wavy bronze bags contain 5 drab green bags, 3 dim plum bags, 4 mirrored lavender bags.
light indigo bags contain 5 dark aqua bags.
shiny bronze bags contain 4 vibrant magenta bags, 2 clear teal bags, 4 muted coral bags.
posh aqua bags contain 2 dotted green bags, 4 bright plum bags, 1 vibrant orange bag.
striped maroon bags contain 5 dotted beige bags, 5 light tomato bags.
bright crimson bags contain 5 vibrant beige bags, 3 faded teal bags, 5 mirrored white bags.
pale green bags contain 4 bright beige bags, 2 posh turquoise bags, 3 mirrored silver bags, 5 dim lime bags.
shiny black bags contain 1 faded yellow bag.
plaid brown bags contain 4 shiny salmon bags, 2 pale bronze bags, 3 dark orange bags.
dim lavender bags contain 5 dotted tan bags, 4 dull maroon bags, 4 striped plum bags, 5 light purple bags.
dim gray bags contain 2 faded tomato bags.
dotted plum bags contain 4 light gray bags, 1 bright turquoise bag, 2 drab maroon bags.
faded purple bags contain 3 vibrant cyan bags, 3 shiny aqua bags.
drab plum bags contain 5 pale chartreuse bags, 1 wavy crimson bag.
muted salmon bags contain 3 pale orange bags, 4 faded yellow bags, 3 dim tomato bags.
posh gold bags contain 2 drab chartreuse bags.
light teal bags contain 2 clear green bags, 2 light violet bags, 1 clear yellow bag, 3 bright turquoise bags.
clear tomato bags contain 1 posh aqua bag, 1 bright beige bag, 5 pale coral bags, 3 mirrored crimson bags.
dull turquoise bags contain 2 plaid coral bags.
striped red bags contain 1 dotted green bag, 2 plaid olive bags, 1 clear crimson bag.
shiny plum bags contain 4 light indigo bags, 4 muted plum bags.
dull indigo bags contain 3 posh white bags, 1 posh green bag, 1 dull plum bag, 5 shiny black bags.
dotted coral bags contain 1 mirrored magenta bag, 2 bright maroon bags, 1 drab tomato bag.
drab indigo bags contain 1 dotted turquoise bag.
posh red bags contain 4 faded blue bags, 2 mirrored green bags.
wavy tan bags contain 3 shiny cyan bags, 1 striped gold bag, 2 dim silver bags, 3 plaid magenta bags.
dim chartreuse bags contain 2 clear bronze bags.
vibrant crimson bags contain 3 faded brown bags, 2 pale chartreuse bags.
plaid yellow bags contain 3 striped brown bags, 1 plaid white bag, 4 vibrant indigo bags.
posh fuchsia bags contain 5 faded bronze bags, 3 drab gray bags.
mirrored red bags contain 3 wavy lime bags, 4 bright tan bags, 5 faded white bags.
shiny coral bags contain 4 wavy yellow bags, 2 bright turquoise bags.
dull beige bags contain 3 posh aqua bags.
posh beige bags contain 1 pale maroon bag, 4 shiny teal bags, 1 clear lime bag.
posh maroon bags contain 1 muted olive bag, 2 dim black bags, 1 plaid cyan bag, 3 dim olive bags.
faded gray bags contain 1 vibrant tomato bag, 4 posh teal bags, 5 striped maroon bags.
dotted cyan bags contain 4 dull orange bags, 2 clear bronze bags, 4 posh gray bags.
bright green bags contain 5 posh tomato bags, 2 wavy red bags.
clear lavender bags contain 3 dark plum bags, 5 dim salmon bags, 2 mirrored magenta bags, 3 plaid silver bags.
muted fuchsia bags contain 5 pale cyan bags.
dark yellow bags contain 3 plaid orange bags, 5 pale lime bags, 2 pale red bags.
bright turquoise bags contain 2 wavy yellow bags.
light bronze bags contain 4 light purple bags.
clear orange bags contain 3 dotted purple bags, 4 plaid fuchsia bags, 1 shiny lime bag.
striped orange bags contain 4 striped red bags, 1 dark bronze bag.
clear brown bags contain 3 light lavender bags, 1 dim plum bag, 5 shiny gray bags.
wavy lavender bags contain 1 pale gray bag, 2 wavy white bags, 3 bright white bags.
bright bronze bags contain 2 shiny turquoise bags, 1 vibrant indigo bag.
dull cyan bags contain 5 plaid orange bags, 4 muted coral bags, 2 bright coral bags, 2 dark olive bags.
faded lime bags contain 4 faded yellow bags, 1 dim lavender bag.
shiny olive bags contain 1 muted olive bag, 4 mirrored turquoise bags, 3 plaid magenta bags.
mirrored tomato bags contain 1 wavy green bag, 1 dotted brown bag, 5 posh magenta bags.
striped cyan bags contain 2 dim teal bags, 3 bright bronze bags, 3 drab chartreuse bags, 4 posh salmon bags.
striped magenta bags contain 2 dark orange bags.
pale white bags contain 1 pale indigo bag.
striped plum bags contain 3 dim plum bags, 4 faded black bags, 1 faded brown bag.
faded brown bags contain 4 clear maroon bags.
mirrored indigo bags contain 2 wavy indigo bags, 2 dull fuchsia bags, 5 bright coral bags.
dark coral bags contain 5 dotted fuchsia bags.
dull fuchsia bags contain 5 pale turquoise bags, 5 dark purple bags, 4 light red bags.
clear chartreuse bags contain 5 dotted turquoise bags.
vibrant gray bags contain 3 plaid orange bags, 2 dotted teal bags.
bright fuchsia bags contain no other bags.
clear salmon bags contain 4 light lime bags, 1 muted black bag, 4 vibrant magenta bags, 1 drab yellow bag.
muted bronze bags contain 3 dull aqua bags, 4 striped turquoise bags.
striped beige bags contain 3 vibrant beige bags.
dim white bags contain 1 mirrored blue bag, 1 vibrant cyan bag, 1 plaid coral bag, 5 light yellow bags.
clear olive bags contain 2 faded teal bags, 1 vibrant orange bag, 4 dim bronze bags.
light purple bags contain 4 dull aqua bags, 1 light gray bag, 2 clear green bags, 4 light fuchsia bags.
mirrored white bags contain 3 faded tomato bags, 5 plaid cyan bags, 2 drab magenta bags.
drab silver bags contain 2 dim plum bags, 5 wavy yellow bags, 2 dull teal bags, 3 bright crimson bags.
dark maroon bags contain 5 mirrored purple bags, 5 light tomato bags.
posh lime bags contain 2 light indigo bags, 3 muted tan bags, 3 shiny coral bags.
pale crimson bags contain 2 dotted tan bags.
plaid turquoise bags contain 4 clear teal bags, 1 light lavender bag, 1 posh salmon bag, 5 light teal bags.
plaid lime bags contain 5 wavy gray bags, 5 dull magenta bags, 3 wavy yellow bags, 1 dim aqua bag.
pale silver bags contain 4 mirrored turquoise bags.
dull gold bags contain 3 mirrored gold bags, 5 vibrant purple bags, 3 light beige bags.
dark purple bags contain 5 wavy yellow bags.
faded lavender bags contain 5 posh bronze bags, 2 vibrant violet bags, 5 drab maroon bags, 3 wavy bronze bags.
dull crimson bags contain 3 muted red bags, 3 muted brown bags.
bright cyan bags contain 3 mirrored chartreuse bags, 5 light fuchsia bags, 2 light tan bags.
drab chartreuse bags contain 5 muted green bags, 1 drab olive bag, 4 clear beige bags.
dull gray bags contain 5 posh fuchsia bags.
bright black bags contain 5 faded brown bags, 3 dim aqua bags, 4 bright violet bags.
faded beige bags contain 5 bright teal bags, 4 faded crimson bags, 3 plaid teal bags.
posh purple bags contain 3 shiny purple bags, 3 plaid turquoise bags.
plaid white bags contain 1 dotted cyan bag.
wavy magenta bags contain 3 vibrant tan bags, 4 posh brown bags, 4 bright tan bags.
dim tomato bags contain 3 drab lime bags, 4 vibrant tomato bags.
mirrored maroon bags contain 3 drab coral bags."""

rule_arr = re.split("\n", rules2)
rules_separated = []
bags = {}
for rule in rule_arr:
	# create array for each rule - 1st element is main bag, others are composite bags, also remove "bag" or "bags" from the end
	baglist = list(" ".join(x.split(" ")[:-1]) for x in list(x for x in re.split(" contain |, |\.", rule) if x!=''))
	# rules_separated.append(baglist)
	if baglist[0] not in bags:
		bags[baglist[0]] = 0
	composite_bags = {}
	for bag in baglist[1:]:
		lst = re.split("([0-9]) ", bag)
		if len(lst)>1:
			composite_bags[lst[2]] = lst[1]
	if composite_bags != {}:
		bags[baglist[0]] = composite_bags
	# print(bags)
	# print(composite_bags)
	
	
# print(rules_separated)
# print("bags: ", bags)
# print("-----------------------------")
# print("bags keys: ", [x for x in bags.keys()])
# print("-----------------------------")
# print("bags values: ", [x for x in bags.values()])
# print("-----------------------------")


bag_arr = []
def findbags(bag, dct):
	val_list = list(dct.values())
	key_list = list(dct.keys())
	for x in [x for x in val_list if x!=0]:
		if bag in x:
			# print("x: ", x)
			super_bag = key_list[val_list.index(x)]
			# print("super_bag: ", super_bag)
			bag_arr.append(super_bag)
			findbags(super_bag, dct)

# findbags("shiny gold", bags)
# print(len(set(bag_arr)))

##### part 2 #########

# print(bags)


## this was asked on reddit
def count(bag='shiny gold'):
	c=0 
# variable to save count
    
	in_current_bag=bags[bag] 
# get the bags inside the bag as provided in the input.
	
	if type(in_current_bag) is dict:
# check if the in_current_bag is a dictionary, because if there are no bags inside a bag, I assigned them 0 directly instead of an empty dictionary.

		for key,value in in_current_bag.items():
# for each bag inside current bag, get the count of bags inside it, recursively.
			
			c+= int(value) + (int(value)*count(key))

# basically if there are 4 white bags in shiny gold bag, I add 4 to c and then add 4*(the count of bags in a white bag).

	return c


print(count("shiny gold"))

