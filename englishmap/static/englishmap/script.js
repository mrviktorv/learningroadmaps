

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

  function replyCollapse(n) {
    var x = document.getElementById("collapseForm" + n);
    if (x.style.display === "none") {
      x.style.display = "block";
      document.getElementById("btn"+n).style.display = "none";
    } 
  }

  function showMore(n) {
    var x = document.getElementById("showmore" + n);
    if (x.style.display === "none") {
      x.style.display = "block";
      document.getElementById("more-btn"+n).innerHTML = "Show less";
    } else {
      x.style.display = "none";
      document.getElementById("more-btn"+n).innerHTML = "Show more";
    }
  }



  bodyh = document.getElementsByTagName("body")[0].scrollHeight
  // console.log(bodyh)
  document.getElementById("grad2").style.height = bodyh-150


  // a function to crop the top image div depending on the size of the window/screen (i may use it later)
  // function height() {
  //   console.log(window.innerHeight)
  // }

  // Get the <span> element that closes the modal
  // var span = document.getElementsByClassName("close")[0];
  
  // When the user clicks on <span> (x), close the modal
  // span.onclick = function() {
  //   modal.style.display = "none";
  // }
  
  // When the user clicks anywhere outside of the modal, close it
  // refactor this code like this: document.querySelectorAll(".card").forEach(card=>{card.style.display = ...
    

