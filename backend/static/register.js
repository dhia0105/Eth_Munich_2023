async function register_event()
{
	const eventName = document.getElementById('eventName').value;
    const eventSymbol = document.getElementById('eventSymbol').value;
    const eventAddress = document.getElementById('eventAddress').value;
	console.log(eventName);
	let body = JSON.stringify({
                    "eventName": eventName,
                    "eventSymbol": eventSymbol,
                    "eventAddress": eventAddress,
                    
                });
        console.log(body);
        await fetch("/home/deploy" ,
	{	
		method: "POST",
		headers:
		{
			'Content-Type': 'application/json'
		},
		mode: 'no-cors',
		body: body
	})
	.catch((e) =>
	{
		console.log(e);
		return;
	})
	.then(response =>
	{
		console.log(response.json);
		return;
	});
    }

