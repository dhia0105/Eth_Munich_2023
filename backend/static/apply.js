async function apply_event(eventName)
{
	const emailAddress = document.getElementById('emailAddress').value;
	const walletApplicant = document.getElementById('walletApplicant').value;
	

	if (eventName){
		let body = JSON.stringify({
						"eventName": eventName,
						"emailAddress": emailAddress,
						"walletApplicant": walletApplicant,
						
					});
			console.log(body);
			await fetch("/event/apply" ,
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
		else{
			console.log("no event name provided");
			return;
		}
}