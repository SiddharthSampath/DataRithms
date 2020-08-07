
function loadURL(){
        console.log("AAAAA")
        const login = document.getElementById('login');
        let link = 'https://';
        const domain = 'datarithms.us.auth0.com';
        const audience = 'datarithms';
        const response = 'token'
        const client_id = 'Y5vM0Nuvm7HJ7U2QRMw5kOtYgyj2jF8L'
        const redirect_uri = 'http://127.0.0.1:5000/login'
        link += domain + '/authorize?';
        link += 'audience=' + audience + '&';
        link += 'response_type=' + response + '&';
        link += 'client_id=' + client_id + '&';
        link += 'redirect_uri=' + redirect_uri;
        login.href = link;
    
    }
  