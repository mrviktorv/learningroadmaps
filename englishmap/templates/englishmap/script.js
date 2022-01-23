  // Automatic Slideshow - change image every x seconds
  // var slideIndex = 0;
  // showSlides();
  
  // function showSlides() {
  //   var i;
  //   var slides = document.getElementsByClassName("mySlides");
  //   for (i = 0; i < slides.length; i++) {
  //     slides[i].style.display = "none";  
  //   }
  //   slideIndex++;
  //   if (slideIndex > slides.length) {slideIndex = 1}    
  //   slides[slideIndex-1].style.display = "block";  
  //   setTimeout(showSlides, 4000); // Change image every 2 seconds
  // }


  // window.onscroll = function() {myFunction1()};

  // var navbar = document.getElementById("navbar");
  // var sticky = navbar.offsetTop;
  
  // function myFunction1() {
  //   if (window.pageYOffset >= sticky) {
  //     navbar.classList.add("sticky")
  //   } else {
  //     navbar.classList.remove("sticky");
  //   }
  // }

  
  // window.addEventListener("scroll", myFunction1);

  // Show/hide the vertical link menu when scrolling 
  // myid = document.getElementById("myid");
  
  // var myScrollFunc = function () {
  //   var y = window.scrollY;
  //     if (y >= 500) {
  //         // myid.className = "vertical-menu show"
  //         myid.classList.remove("hide")
  //         myid.classList.add("show")
  //     } else {
  //         // myid.className = "vertical-menu hide"
  //         myid.classList.remove("show")
  //         myid.classList.add("hide")
  //     }
  // };
  
  // window.addEventListener("scroll", myScrollFunc);


// this can be refactored with getelementsbyclass(...)[n] and use it to change buton and div instead of numbered el id's
  function collapse(n) {

      var x = document.getElementById("collapse" + n);
      if (x.style.display === "none") {
        x.style.display = "block";
        document.getElementById("btn"+n).innerHTML = "hide";
      } else {
        x.style.display = "none";
        document.getElementById("btn"+n).innerHTML = "show";
      }
  }

  // a function to crop the top image div depending on the size of the window/screen (i may use it later)
  // function height() {
  //   console.log(window.innerHeight)
  // }

  // function openmodal(n) {
  //     var modal = document.getElementById("myModal"+ n);
  //     modal.style.display = "block";
  // }


  
  // Get the <span> element that closes the modal
  // var span = document.getElementsByClassName("close")[0];
  
  // When the user clicks on <span> (x), close the modal
  // span.onclick = function() {
  //   modal.style.display = "none";
  // }
  
  // When the user clicks anywhere outside of the modal, close it
  // refactor this code like this: document.querySelectorAll(".card").forEach(card=>{card.style.display = ...
    
  window.onclick = function(event) {
    elNum = document.getElementsByClassName("modal").length
    for (let i = 0; i < elNum; i++) {
      let currentModal = document.getElementsByClassName("modal")[i];
      if (event.target == currentModal) {
        currentModal.style.display = "none";
      }
    }
  }

  // create all grid layout
  for (let i = 0; i < 9; i++) {
  
    let newdiv = document.createElement("div") 
    let dan = `
      <div class="grid-container">
  <div class="item1">
    <div class="random">
      <div class="arrow left">
      </div>
    </div>
  </div>
  <div class="item2">
    <div class="random">
      <div class="arrow center">
      </div>
    </div>
  </div>
  <div class="item3">
    <div class="random">
      <div class="arrow right">
      </div>
    </div>
  </div>  
  <div class="item4">
    <div class="random left">
    </div>
  </div>
  <div class="item5">
    <div class="random center">
    </div>
  </div>
  <div class="item6">
    <div class="random right">
      </div>
    </div>
  </div>
    
</div>
  `
  document.getElementById("layout").appendChild(newdiv);
  newdiv.innerHTML = dan;
  }

  for (let i = 0; i < 2; i++) {
  
    let newdiv = document.createElement("div") 
    let dan = `
      <div class="grid-container">
  <div class="item1">
    <div class="random">
      <div class="arrow left">
      </div>
    </div>
  </div>
  <div class="item2">
    <div class="random">
      <div class="arrow center">
      </div>
    </div>
  </div>
  <div class="item3">
    <div class="random">
      <div class="arrow right">
      </div>
    </div>
  </div>  
  <div class="item4">
    <div class="random left">
    </div>
  </div>
  <div class="item5">
    <div class="random center">
    </div>
  </div>
  <div class="item6">
    <div class="random right">
      </div>
    </div>
  </div>
    
</div>
  `
  document.getElementById("layout2").appendChild(newdiv);
  newdiv.innerHTML = dan;
  }

  
  // slightly randomize the card's position (put all paddings into 1 padding: x x x x)
  document.querySelectorAll(".random").forEach(random=>{
    random.style.paddingTop = Math.floor(Math.random() * 20) + "px";
    random.style.paddingLeft = Math.floor(Math.random() * 20) + "px";
    random.style.paddingRight = Math.floor(Math.random() * 20) + "px";
    random.style.paddingBottom = Math.floor(Math.random() * 20) + "px";
  })
  
  

  // make IF check for unidentified and null
  const allGrids = document.getElementsByClassName("grid-container")
  for (grid in allGrids) {
      let arroL = document.getElementsByClassName("arrow left")[grid]
      if (setLayout[grid].arrL != '') {
      arroL.innerHTML = `<img src="images/${setLayout[grid].arrL}.png" class="img-arrow">`
      }
      let arroC = document.getElementsByClassName("arrow center")[grid]
      if (setLayout[grid].arrC != '') {
      arroC.innerHTML = `<img src="images/${setLayout[grid].arrC}.png" class="img-arrow">`
      }
      let arroR = document.getElementsByClassName("arrow right")[grid]
      if (setLayout[grid].arrR != '') {
      arroR.innerHTML = `<img src="images/${setLayout[grid].arrR}.png" class="img-arrow">`
      }
      // src="{% static 'englishmap/${setLayout[grid].arrR}.png' %}"
     

      // find the right topic by its ID from setLayout and put the data into the card
      let topiL = document.getElementsByClassName("random left")[grid]
      let setL = setLayout[grid].topL
      if (setL > 0) {
      let currTopic = topics.find(x => x.id == setL)
      topiL.innerHTML = `<div class="topic-card" onclick="openmodal(${setL})">
      <h4>${currTopic.topic} <span class="span-id">${setL}<span></h4>
      <hr>
      <p>${currTopic.short}</p>
      </div>`
      }

      let topiC = document.getElementsByClassName("random center")[grid]
      let setC = setLayout[grid].topC
      if (setC > 0) {
      let currTopic = topics.find(x => x.id == setC)
      topiC.innerHTML = `<div class="topic-card" onclick="openmodal(${setC})">
      <h4>${currTopic.topic} <span class="span-id">${setC}<span></h4>
      <hr>
      <p>${currTopic.short}</p>
      </div>`
      }

      let topR = document.getElementsByClassName("random right")[grid]
      let setR = setLayout[grid].topR
      if (setR > 0) {
      let currTopic = topics.find(x => x.id == setR)
      topR.innerHTML = `<div class="topic-card" onclick="openmodal(${setR})">
      <h4>${currTopic.topic} <span class="span-id">${setR}</h4>
      <hr>
      <p>${currTopic.short}</p>
      </div>`
      }

  }
  function openmodal(n) {
      var modal = document.getElementById("myModal");
      modal.style.display = "block";
      let obj = topics.find(x => x.id == n)
      // let obj = topics[n-1]
  document.getElementById("c").innerHTML = obj.topic;
  document.getElementById("d").innerHTML = obj.short;
  document.getElementById("e").innerHTML = obj.full;
  document.getElementById("f").innerHTML = `"#" + ${obj.id};`
  }



