
const logIn = document.getElementById("log__in")
const signIn = document.getElementById("sign__in")
const formLogIn = document.getElementById("form")
const formSignIn = document.getElementById("form__sign")
const closeBtn = document.getElementById("close__modal1")
const closeBtn2 = document.getElementById("close__modal2")
const btn1 = document.getElementById('submit')

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




btn1.addEventListener('click', (e) => {
    e.preventDefault()

    const login = document.getElementById('login1').value
    const password = document.getElementById('password1').value

    fetch('https://7669-188-186-201-27.ngrok-free.app/api/signin', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "ngrok-skip-browser-warning":'69420',
            "Accept": 'application/json',

        },
        body: JSON.stringify({
            login:login,
            password:password
        })
    })

        .then(response => response.json())
        .then(data=>{
            const jsonString = JSON.stringify(data)
            console.log(data)
            if (data.first_name) {

                localStorage.setItem('user', jsonString)
                setTimeout(() => {
                    location.assign('./pc/index.html')
                }, 1000)
            } else{
                alert('err')
            }

        })





})
