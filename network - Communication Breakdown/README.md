# Communication Breadown - 50 pts

>"I can't do it anymore", thought Twardowski. "Being a prisoner is one thing, I can handle being alone. But these attacks... I don't deserve this. I'm still suffering from a stupid mistake I made two centuries ago..."

Given: `communication_breakdown.pcapng` file shall be opened by Wireshark tool for ...
This is a record of ~7seconds communication beween two hosts:
<img src="[drawing](https://user-images.githubusercontent.com/8276484/174589533-63210d74-9ce9-4d55-bf1e-467d97093fb9.png)" alt="drawing" width="200"/>

We can see there following steps:
- login procedure to some ftp server
- request of a `flag.zip` file
- response with requested file

To see this communication clearly, you can right-click on a first TCP packet -> Follow -> TCP Stream. You will see human-readable communication from a TCP stream. ( Remember to clear display filter at the top of Wireshark to see all communication again).
