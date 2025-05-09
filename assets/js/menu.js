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
    x = x.slice(0,5)
    x[0] = parseInt(x[0])
    x[1] = x[1].slice(2,-1)
    x[2] = parseInt(x[2])
    x[3] = x[3].slice(2, -1)
    x[4] = x[4].slice(2, -2)
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
    document.getElementById('allitems').style.display = 'none'
    curr_cat = changeto
}

function cart(id,item,price)
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
    { cart_items.push([id,item,price,1])}
    document.getElementById('cart').innerHTML = ''
    document.getElementById('cart').style.display = 'flex'
    for(let i = 0;i < cart_items.length;i++)
    {
       document.getElementById('cart').innerHTML += `<div id="cartp">
        <p id="id" style="display:none;">${cart_items[i][0]}</p>
        <p id="name">${cart_items[i][1]}</p>
        <p id="price">${cart_items[i][2]}₹</p>
        <button id="min" onclick="dec(this)"><i class="fa-solid fa-minus"></i></button>
        <p id="no_of">${cart_items[i][3]}</p>
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
  cart_items = cart_items.map((item) => [item[1], item[2],item[3]]);
  for(let i of cart_items)
{ list_of_items += ';' + i.toString()}
  var data = {
    items: list_of_items.slice(1)
  };
  $.ajax({
    url: 'http://127.0.0.1:5000/final/',
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
      { let x = i[1].toLowerCase()
      if(x.startsWith(ser) || i[1].startsWith(ser))
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
if(i[4] == 'Available')
{
document.getElementById("allitems").innerHTML += `<div id="items">
    <p class="item_id">${i[0]}</p>
    <p class="availability">${i[4]}</p>
    <p class="item_message">This item is temporarily unavailable</p>
        <img id="img" src="/static/images/${i[3]}" alt="images/${i[3]}">
        <div>
            <p id="pname">${i[1]}</p>
            <p class="p"><span>Price&nbsp;:</span><span class="red">&nbsp;${i[2]}₹</span></p>
            <p class="p"><span>Rating:&nbsp;&nbsp;</span><span class="red">4.5&nbsp;&nbsp;</span><i
                    class="fa-solid fa-star" id="star"></i></p>
        </div>
    <button onclick="cart('${i[1]}','${i[2]}')">Add to cart</button>
  </div>`;
}
else
{
document.getElementById("allitems").innerHTML += `<div id="items" class="mask">
  <p class="item_id">${i[0]}</p>
        <p class="availability">${i[4]}</p>
        <p class="item_message">This item is temporarily unavailable</p>
            <img id="img" src="/static/images/${i[3]}" alt="images/${i[3]}">
            <div>
                <p id="pname">${i[1]}</p>
                <p class="p"><span>Price&nbsp;:</span><span class="red">&nbsp;${i[2]}₹</span></p>
                <p class="p"><span>Rating:&nbsp;&nbsp;</span><span class="red">4.5&nbsp;&nbsp;</span><i
                        class="fa-solid fa-star" id="star"></i></p>
            </div>
            <button onclick="cart('${i[1]}','${i[2]}')">Add to cart</button>
        </div>`;
}
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
{  document.getElementById('divcart').style.display = 'flex' }
else
{  document.getElementById('divcart').style.display = 'none' }
}
appetizers = document.getElementById("Appetizers");
soups_salads = document.getElementById("Soups_salads");
rice_items = document.getElementById("Rice_items");
breads_rotis = document.getElementById("Breads_rotis");
special_curries = document.getElementById("Special_curries");
side_dishes = document.getElementById("Side_dishes");
deserts = document.getElementById("Deserts");
drinks = document.getElementById("Drinks");
menu = {appetizers: appetizers,soups_and_salads: soups_salads,
  rice_items: rice_items,breads_rotis: breads_rotis,special_curries: special_curries,
  side_dishes: side_dishes,deserts: deserts,drinks: drinks,};

function update(data)
{
  let div = menu[data.category]
  let divs = div.querySelectorAll('#items')
  let id1 = data.item[0][0].toString();
  for(let div of divs)
  { let id = div.querySelector(".item_id").innerHTML;
    if(id[0] == "'")
    {id = id.slice(1,-1)}
    if(id1 == id)
    {
      div.querySelector('#pname').innerHTML = data.item[0][1]
      div.querySelector('.red').innerHTML =  `${data.item[0][2]}₹`
      if (data.item[0][4] == "Unavailable")
      {  div.classList.add("mask");
      for(let i in cart_items)
      {
        if(id1 == cart_items[i][0])
        {
          cart_items.splice(i,1)
          let cartdiv = document.getElementById('cart')
          let cartdivs = cartdiv.querySelectorAll('#cartp')
          for(let x of cartdivs)
          {
            let cart_id = x.querySelector('#id').innerHTML
            if(id1 == cart_id)
            {
              x.style.textDecoration = "line-through";
              x.style.color = "red";
              x.title = 'This item is currently unavailable'
              total -= parseInt(x.querySelector('#price').innerHTML)
              document.getElementById('pricet').innerHTML = total
            }
          }
        }
      }
      }
      else {  div.classList.remove("mask");  }
      }
    }

  div = document.getElementById('allitems')
  divs = div.querySelectorAll('#items')
  for(let div of divs)
  {
    id = div.querySelector('#pname').innerHTML
    if(id == data.item[0][1])
    {div.classList.add('mask')}
    else
    {div.classList.remove('mask')}
  }
  for(let i of list)
  {
    if(i[1] == data.item[0][1])
    { i[4] = data.item[0][4] }
  }
  }

function del(data)
{
  let div1 = menu[data.category];
  let divs = div1.querySelectorAll("#items");
  let id1 = data.item[0][0].toString();
  for (let div of divs) {
    let id = div.querySelector(".item_id").innerHTML;
    if (id[0] == "'") {
      id = id.slice(1, -1);}
    if (id1 == id) {
      div1.removeChild(div)
    }
  }
for (let i in cart_items) {
  if (cart_items[i][0] == id1) {
    cart_items.splice(i,1)
    let cartdiv = document.getElementById('cart')
    let cartdivs = cartdiv.querySelectorAll('#cartp')
    for(let x of cartdivs)
    {
      let cart_id = x.querySelector('#id').innerHTML
      if(id1 == cart_id)
      {
        console.log('equal')
        x.style.textDecoration = "line-through";
        x.style.color = "red";
        x.title = "This item is deleted from Menu";
        total -= parseInt(x.querySelector("#price").innerHTML);
        document.getElementById("pricet").innerHTML = total;
      }
    }
  }
}
}

function add_item(data)
{
  let div = menu[data.category];
  if (data.item[0][4] == "Unavailable") {
    div.innerHTML += `<div id="items" class="mask">
  <p class="item_id">${data.item[0][0]}</p>
        <p class="availability">${data.item[0][4]}</p>
        <p class="item_message">This item is temporarily unavailable</p>
            <img id="img" src="/static/images/${data.item[0][3]}" alt="images/${data.item[0][3]}">
            <div>
                <p id="pname">${data.item[0][1]}</p>
                <p class="p"><span>Price&nbsp;:</span><span class="red">&nbsp;${data.item[0][2]}₹</span></p>
                <p class="p"><span>Rating:&nbsp;&nbsp;</span><span class="red">4.5&nbsp;&nbsp;</span><i
                        class="fa-solid fa-star" id="star"></i></p>
            </div>
            <button onclick="cart('${data.item[0][1]}','${data.item[0][2]}')">Add to cart</button>
        </div>`;
  } else {
    div.innerHTML += `<div id="items" class="items">
        <p class="item_id">${data.item[0][0]}</p>
        <p class="availability">${data.item[0][4]}</p>
        <p class="item_message">This item is temporarily unavailable</p>
            <img id="img" src="/static/images/${data.item[0][3]}" alt="images/${data.item[0][3]}">
            <div>
                <p id="pname">${data.item[0][1]}</p>
                <p class="p"><span>Price&nbsp;:</span><span class="red">&nbsp;${data.item[0][2]}₹</span></p>
                <p class="p"><span>Rating:&nbsp;&nbsp;</span><span class="red">4.5&nbsp;&nbsp;</span><i
                        class="fa-solid fa-star" id="star"></i></p>
            </div>
            <button onclick="cart('${data.item[0][1]}','${data.item[0][2]}')">Add to cart</button>
        </div>
  `;
  }
list.push(data.item)
console.log(list)
}

const socket = new WebSocket("ws://" + window.location.host + "/ws/Menu/");
socket.onopen = function (e) {
};

socket.onmessage = function (event) {
  let data = JSON.parse(event.data);
  data = data['message']['message']
  if(data['type'] == 'update')
  {update(data)}
  if(data['type'] == 'delete')
  {del(data)}
  if(data['type'] == 'new item')
  {add_item(data)}
};

socket.onclose = function (event) {
};

socket.onerror = function (error) {
};

