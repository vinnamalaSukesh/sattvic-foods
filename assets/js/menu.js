var curr_cat = 'Appetizers'
var cart_items = []
var total = 0
var itemslist = document.getElementById('itemslist').textContent
itemslist = itemslist.slice(2,itemslist.length - 2)
itemslist = itemslist.split('[')
list = []
var list_of_items = ''
for (let i of itemslist)
{
    let x = (i.split(','))
    x = x.slice(0,3)
    x[0] = x[0].slice(1,-1)
    x[1] = parseInt(x[1])
    x[2] = x[2].slice(2,-2)
    list.push(x)
}
function change(changeto)
{
    document.getElementById(changeto + 'b').style.backgroundColor = 'rgb(250, 244, 245)';
    document.getElementById(changeto + 'b').style.color = 'red';
    document.getElementById(changeto + 'b').style.borderColor = 'red';
    document.getElementById(changeto + 'b').style.boxShadow = '0px 0px 5px red';
    document.getElementById(changeto).style.display = 'flex'

    document.getElementById(curr_cat + 'b').style.backgroundColor = 'white';
    document.getElementById(curr_cat + 'b').style.color = 'black';
    document.getElementById(curr_cat + 'b').style.borderColor = 'white';
    document.getElementById(curr_cat + 'b').style.boxShadow = '0px 0px 5px white';
    document.getElementById(curr_cat).style.display  = 'none'
    curr_cat = changeto
}

function cart(item,price)
{   var x = 0;
    total += parseInt(price);
    for(let i of cart_items)
    {
        if(i[0] == item)
        { i[2] += 1
          x = 1
        }
    }
    if(x != 1)
    { cart_items.push([item,price,1])}
    document.getElementById('cart').innerHTML = ''
    document.getElementById('cart').style.display = 'flex'
    for(let i = 0;i < cart_items.length;i++)
    {
       document.getElementById('cart').innerHTML += `<div id="cartp">
  <p id="name">${cart_items[i][0]}</p>
  <p id="price">${cart_items[i][1]}₹</p>
  <button id="min" onclick="dec(this)"><i class="fa-solid fa-minus"></i></button>
  <p id="no_of">${cart_items[i][2]}</p>
  <button id="plus" onclick="inc(this)"><i class="fa-solid fa-plus"></i></button>
  </div>`
    }
    document.getElementById('cart').innerHTML += `<div>
  <p id="namet">Total : </p><p id="pricet">${total}₹</p>
  </div>`
}

function dec(button)
{
    let ele =  $(button).siblings();
    let count = ele[2].innerText;
    ele[2].innerHTML = parseInt(count) - 1;
    let item = ele[0].innerText;
    for(let i = 0;i < cart_items.length;i++)
    {
        if(item == cart_items[i][0])
        {
        if(cart_items[i][2] == 1)
        { cart_items.splice(i,1) }
        else
        { cart_items[i][2] = parseInt(count) - 1 }
        }
    }
    document.getElementById('cart').innerHTML = ''
    total = 0
    if(cart_items.length  == 0)
    {document.getElementById('cart').style.display = 'none'}
    else
    {for(let i = 0;i < cart_items.length;i++)
    {  total += parseInt(cart_items[i][1] * cart_items[i][2])
       document.getElementById('cart').innerHTML += `<div id="cartp"><p id="name">${cart_items[i][0]}</p>  <p id="price">${cart_items[i][1]}₹</p><button id="min" onclick="dec(this)"><i class="fa-solid fa-minus"></i></button><p id="no_of">${cart_items[i][2]}</p><button id="plus" onclick="inc(this)"><i class="fa-solid fa-plus"></i></button></div>`
    }
    document.getElementById('cart').innerHTML += `<div><p id="namet">Total : </p><p id="pricet">${total}₹</p> </div>`
}}

function inc(button)
{
    var ele = $(button).siblings();
    let count = ele[3].innerText;
    ele[3].innerHTML = parseInt(count) + 1;
    for(let i = 0;i < cart_items.length;i++)
    {
        if(cart_items[i][0] == ele[0].innerText)
        { cart_items[i][2] += 1  }
    }
    total = 0
    document.getElementById('cart').innerHTML = ''
    for(let i = 0;i < cart_items.length;i++)
    {  total += parseInt(cart_items[i][1]) * cart_items[i][2]
       document.getElementById('cart').innerHTML += `<div id="cartp"><p id="name">${cart_items[i][0]}</p>  <p id="price">${cart_items[i][1]}₹</p><button id="min" onclick="dec(this)"><i class="fa-solid fa-minus"></i></button><p id="no_of">${cart_items[i][2]}</p><button id="plus" onclick="inc(this)"><i class="fa-solid fa-plus"></i></button></div>`
    }
    document.getElementById('cart').innerHTML += `<div><p id="namet">Total : </p><p id="pricet">${total}₹</p> </div>`
}

function send()
{ let list_of_items = ''
  for(let i of cart_items)
{ list_of_items += ';' + i.toString()}

  var data = {
    items: list_of_items.slice(1)
  };
  $.ajax({
    url: 'http://127.0.0.1:8000/final/',
    type: 'GET',
    data: data,
    success: function(response) {
      console.log('Response from server:', response);
    },
    error: function(xhr, status, error) {
      console.log('An error occurred:', error);
    }
    });
}

function search()
{
    let ser = document.getElementById('search').value
    if(ser == '')
    {
    document.getElementById('Appetizers' + 'b').style.backgroundColor = 'rgb(250, 244, 245)';
    document.getElementById('Appetizers' + 'b').style.color = 'red';
    document.getElementById('Appetizers' + 'b').style.borderColor = 'red';
    document.getElementById('Appetizers' + 'b').style.boxShadow = '0px 0px 5px red';
    document.getElementById('Appetizers').style.display = 'flex'
    document.getElementById('allitems').style.display = 'none'
    curr_cat = 'Appetizers'
    }
    else
    { var sortlist = []
      for(let i of list)
      { let x = i[0].toLowerCase()
      if(x.startsWith(ser))
      {sortlist.push(i)}
      }
    document.getElementById('allitems').style.display = 'flex'
    document.getElementById(curr_cat + 'b').style.backgroundColor = 'white';
    document.getElementById(curr_cat + 'b').style.color = 'black';
    document.getElementById(curr_cat + 'b').style.borderColor = 'white';
    document.getElementById(curr_cat + 'b').style.boxShadow = '0px 0px 5px white';
    document.getElementById(curr_cat).style.display  = 'none'
    curr_cat = 'All'
document.getElementById('allitems').innerHTML = ''
for (let i of sortlist)
{
document.getElementById('allitems').innerHTML +=
`<div id='items'><img src='/static/images/${i[2]}' class='iimg'>
<div>
<p>${i[0]}</p>
<p class="p"><span>Price&nbsp;:</span><span class="red">&nbsp; ${i[1]}₹</span></p>
<p class="p"><span>Rating:&nbsp;&nbsp;</span><span class="red">4.5&nbsp;&nbsp;</span><i class="fa-solid fa-star" id="star"></i></p>
</div>
<button onclick="cart('${i[0]}','${i[1]}')">Add to cart</button>
</div>`
}
}
}

function log()
{
if(document.getElementById('loga').style.display === 'none' || document.getElementById('loga').style.display === '')
{  document.getElementById('loga').style.display = 'flex'  }
else
{  document.getElementById('loga').style.display = 'none'  }
}

function rem()
{
document.getElementById('loga').style.display = 'none'
}

function cartdis()
{
if(document.getElementById('divcart').style.display === '' || document.getElementById('divcart').style.display === 'none')
{ console.log('noned')
document.getElementById('divcart').style.display = 'flex' }
else
{ console.log('flexd')
document.getElementById('divcart').style.display = 'none' }
}