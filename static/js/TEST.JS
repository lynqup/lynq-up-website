var templateParams = {
    from_name: 'from',
    from_email: 'mail',
    phone: 'phone',
    subject: 'Geen onderwerp',
    message: 'message TEST'
        };
emailjs.send('service_gbyev38', 'template_ty0126l', templateParams), then(
    (response) => {
        console.log('SUCCESS!', response.status, response.text);
    },
    (error) => {
        console.log('FAILED...', error);
    },
    );