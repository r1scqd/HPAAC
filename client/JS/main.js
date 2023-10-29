
const logIn = document.getElementById("log__in")
const signIn = document.getElementById("sign__in")
const formLogIn = document.getElementById("form")
const formSignIn = document.getElementById("form__sign")
const closeBtn = document.getElementById("close__modal1")
const closeBtn2 = document.getElementById("close__modal2")

logIn.addEventListener("click", function(event) {
    event.preventDefault();
    formLogIn.style.display = "block";
    document.body.classList.add("modal-open");
});

closeBtn.addEventListener("click", function(event) {
    event.preventDefault();
    formLogIn.style.display = "none";
    document.body.classList.remove("modal-open");
});


signIn.addEventListener("click", function(event) {
    event.preventDefault();
    formSignIn.style.display = "block";
    document.body.classList.add("modal-open");
});

closeBtn2.addEventListener("click", function(event) {
    event.preventDefault();
    formSignIn.style.display = "none";
    document.body.classList.remove("modal-open");
});
