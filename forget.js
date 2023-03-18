const username = document.getElementById("username");
const email_id = document.getElementById("email_id");
// const otp1 = document.getElementById("otp1");

let user_id_list = [];
let email_list = [];
let password_list = [];
let temp = {    };
let request = new XMLHttpRequest();
request.open("POST", `/home/api/${JSON.stringify(temp)}`);
request.onload = () => {
    let flaskMsg = request.responseText;
    let msg = flaskMsg.split(",");
    msg.forEach((val) => {
        let tempA = val.split(" - ");
        user_id_list.push(tempA[1]);
        email_list.push(tempA[9]);
        password_list.push(tempA[15]);
        console.log(user_id_list);
        console.log(email_list);
        console.log(password_list);
    });
}
request.send()

function sendEmail() {
    let i = email_list.indexOf(` ${email_id.value} `, 0);
    let params = {
        name: username.value,
        email: email_id.value,
        message: `Your UserId and Password: \n 
                ${user_id_list[i]} \n ${password_list[i]} \n
                \n Don't Share it With Anyone`
    };
    const serviceId = "service_5qsx9ig";
    const templateId = "template_4mcj2bo";

    emailjs.send(serviceId, templateId, params).then((res) => {
      username.value = "";
      email_id.value = "";
    });
}


document.querySelector(".submit").addEventListener("click", function (e) {
    e.preventDefault();
    if (!(user_id_list.includes(` ${username.value} `) || email_list.includes(` ${username.value} `))) {
        alert("Your Username is Not Valid MEANS Not in Records");
    } else {
        sendEmail();
        window.location.assign("/home");
    }

});

document.querySelector(".btn_verify").addEventListener("click", function (e) {
    e.preventDefault();
  if (!(email_list.includes(` ${email_id.value} `))) alert("Email is Not in records");
  else {
    document.querySelector(
      ".btn_verify"
    ).innerHTML = `<h2>Your Password and Details will send by Email to you</h2>`;
  }
});
