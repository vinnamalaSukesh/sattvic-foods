function see(event)
{ event.preventDefault()
  let t = document.getElementById('password').type
  console.log(t)
  if(t == 'password')
  {
    document.getElementById('password').type = 'text'
  }
  else
  {
    document.getElementById('password').type = 'password'
  }
}

var emails = document.getElementById('emails').textContent
var passwords = document.getElementById('passwords').textContent
emails = emails.replace(/\[|\]/g, '').trim();
passwords = passwords.replace(/\[|\]/g, '').trim();
emails = emails.split(',')
passwords = passwords.split(',')
for(let i in emails)
{
    emails[i] = emails[i].replace(/['"]+/g, '').trim();
}
for(let i in passwords)
{
    passwords[i] = passwords[i].replace(/['"]+/g, '').trim();
}

function validate(event)
{
    var email = document.getElementById('email').value
    var password = document.getElementById('password').value
    for(let i in emails)
    {
        if((emails[i] === email) && (passwords[i] === password))
        {   return true;   }
    }
    document.getElementById('msg').style.visibility = 'visible'
    return false;
}