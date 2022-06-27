# Sensors - 50

Required challenge: Manual

>Twardowski was looking at the computers in the command center. The situation was looking extremely bad. The attack started 19 days ago and there were more and more ships comming. This time the Devil stepped up his game - he was no longer tormenting Twardowski by himself. He made it a game to take over his house in exile, Planet Rome.
>
>Suddenly, a distorted message appeared on Twardowski's sensors: /custom/sensors.php.
>
> Flag: Ender's message

`custom/sensors.php` was not available through source code viewer, but can be accessed directly: `https://uni1.cursednova.securing.pl/custom/sensors.php`

There was only one message given, without any clue in a source code:

`O CWME IH PZAOE. PKZ JA ZICURP TBY SGNDINP. EDDER`

Looks like a Caesar Cipher, but `EDDER` is too close to  `ENDER`. Maybe some characters are swapped or replaced? The only thing I can do is to refresh the page and check result:

`T CHPE IN KAACE. ARY NO SBVSRE KHE LOIMIEV. ENKSO`
`Y TOGE IN PMATE. HRG FO SEUURE TDZ LABDING. JNXMR`
`F COME FH EVAXE. BJA TZ SACURE VHW LANDQNP. SNNCR`
`I COHE IQ PTAKN. GRY ZP NCSURT THE LBFXINZ. ENLEP`

See some pattern, fist part is probably: I COME IN PEACE.

Many refresh later, next part becomes clear:

`I COME IN PEACE. TRY TO SECURE THE LANDING.
