// Authentication JS
async function registerUser(email,password){
    const res = await fetch('/auth/register',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({email,password})
    });
    return await res.json();
}

async function loginUser(email,password){
    const res = await fetch('/auth/login',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({username:email,password})
    });
    return await res.json();
}
