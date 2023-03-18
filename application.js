const user_idEl = document.querySelector(".userid");
const f_nameEl = document.querySelector(".fname");
const m_nameEl = document.querySelector(".mname");
const l_nameEl = document.querySelector(".lname");
const father_husbandEl = document.querySelector(".fatherhusband");
const motherEl = document.querySelector(".mother");
const emailEl = document.querySelector(".email_id");
const phone_noEl = document.querySelector(".phone");
const alt_phone_noEl = document.querySelector(".alt_phone");
const aadharEl = document.querySelector(".aadhar");
const dateOBEl = document.querySelector(".dateOB");
const gender2El = document.querySelector(".gender"); 
const maritalEl = document.querySelector(".marital");
const pan_noEl = document.querySelector(".pan");
const castEl = document.querySelector(".cast");
const bloodEl = document.querySelector(".blood");
const qualificationEl = document.querySelector(".qualification");
const address_oneEl = document.querySelector(".address_one");
const address_twoEl = document.querySelector(".address_two");
const state2El = document.querySelector(".state");
const district2El = document.querySelector(".district");
const pinEl = document.querySelector(".pin");
const jobEl = document.querySelector(".job");
const departmentEl = document.querySelector(".department");
const appointmentEl = document.querySelector(".appointment");
const appoint_dateEl = document.querySelector(".appointDate");
const retire_dateEl = document.querySelector(".retireDate");
const memberEl = document.querySelector(".member");
const imgNameEl = document.querySelector(".imgName");
const allInputBoxes = document.querySelectorAll(".input-box");
const user_name = document.getElementById("username");
const pass_word = document.getElementById("password");
let stateList = [];
let distList = [];
let already_users = [];
let fileElement = document.getElementById("upload");
let file_name;
  // check if user had selected a file
let request3 = new XMLHttpRequest();
let temp = {};
request3.open("POST", `/static/applica/${JSON.stringify(temp)}`);
request3.onload = () => {
  let flaskMsg = request3.responseText;
  let msg = flaskMsg.split(",");
  msg.forEach((val) => {
    let tempA = val.split(" - ");
    already_users.push(tempA[3]);
  });
};
request3.send();

fetch("/api/StateDistrictOfpasswordVed@123")
  .then((res) => res.json())
  .then((data) => {
    const countryData = data;
    countryData.states.forEach((st) => stateList.push(st.state));
    let html = "";
    stateList.forEach((st) => (html += `<option>${st}</option>`));
    state2El.insertAdjacentHTML("beforeend", html);
    state2El.addEventListener("change", function () {
      let stateChoice = state2El.value;
      countryData.states.forEach((st) => {
        if (st.state == stateChoice) {
          distList = [];
          distList.push(...st.districts);
          let html2 = "<option disabled selected>Select District</option>";
          distList.forEach((ds) => (html2 += `<option>${ds}</option>`));
          district2El.innerHTML = html2;
        }
      });
    });
  });
  let user_id_list = [];
  let email_list = [];
  let password_list = [];
  function getInfo() {
    var temp = {
      img_name: "file_name",
      title_post: "titleFile",
      descri_post: `ved`,
      first_name: "firstn",
      last_name: "lastn",
    };
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
      });
    };
    request.send();
  }
  getInfo();

let application_info = {};

document.querySelector(".submit").addEventListener("click", function () {
  if (fileElement.files.length === 0) {
    alert("please choose a file");
  } else {

    let file = fileElement.files[0];
    let pre = `${String(file.name).split(".").slice(-1)}`;
    let d = Date.now();
    if (pre.toLowerCase() == "jpg" || pre.toLowerCase() == "png" || pre.toLowerCase() == "jpeg") {
      let formData = new FormData();
      file_name = `UserFile2-${d}.${pre}`;
      formData.append("file", file, file_name);

      axios
        .post("http://localhost:3001/upload-single-file", formData, {
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total);
            console.log(`upload process: ${percentCompleted}%`);
          },
        })
        .then((res) => {
          console.log(res.data);
        });
    }
  }  


  if ((already_users.includes(` ${user_name.value} `))) {
    alert("This user ALREADY Filled Application Form");
  }
  // else if (
  //   phone_noEl.value.length != 10 ||
  //   alt_phone_noEl.value.length != 10
  // ) {
  //   alt_phone_noEl.value = "";
  //   phone_noEl.value = "";
  //   alert("incorrect Phone No.");
  // }
  // else if (
  //   f_nameEl.value == "" ||
  //   m_nameEl.value == "" ||
  //   l_nameEl.value == "" ||
  //   father_husbandEl.value == "" ||
  //   motherEl.value == "" ||
  //   aadharEl.value == "" ||
  //   dateOBEl.value == "" ||
  //   gender2El.value == "" ||
  //   maritalEl.value == "" ||
  //   pan_noEl.value == "" ||
  //   castEl.value == "" ||
  //   bloodEl.value == "" ||
  //   qualificationEl.value == "" ||
  //   address_oneEl.value == "" ||
  //   address_twoEl.value == "" ||
  //   pinEl.value == "" ||
  //   jobEl.value == "" ||
  //   departmentEl.value == "" ||
  //   appointmentEl.value == "" ||
  //   appoint_dateEl.value == "" ||
  //   retire_dateEl.value == "" ||
  //   memberEl.value == ""
  // ) {
  //   alert("Anything is missed by You!!");
  // }
  // else if (
  //   state2El.value == "Select State" ||
  //   district2El.value == "Select District"
  // ) {
  //   alert("State and District is empty");
  // }
  else {
    
    document.querySelectorAll(".input-box").forEach((event) => {
      application_info[event.children[1].className] = event.children[1].value;
    });
    console.log("setTimeOut");
    setTimeout(() => {
    function sendInfo() {
      let info = {
        user_id2: application_info.userid,
        f_name: application_info.fname,
        m_name: application_info.mname,
        l_name: application_info.lname,
        father_husband: application_info.fatherhusband,
        mother: application_info.mother,
        email_id: application_info.email_id,
        phone_no: application_info.phone,
        alt_phone_no: application_info.alt_phone,
        aadhar: application_info.aadhar,
        dateOB: application_info.dateOB,
        gender2: application_info.gender,
        marital: application_info.marital,
        pan_no: application_info.pan,
        cast: application_info.cast,
        blood: application_info.blood,
        qualification: application_info.qualification,
        address1: application_info.address_one,
        address2: application_info.address_two,
        state2: application_info.state,
        district2: application_info.district,
        pin: application_info.pin,
        job: application_info.job,
        department: application_info.department,
        appointment: application_info.appointment,
        appoint_date: application_info.appointDate,
        retire_date: application_info.retireDate,
        member: application_info.member,
        imgName: file_name,
      };
        let request2 = new XMLHttpRequest();
        request2.open("POST", `/static/application/${JSON.stringify(info)}`);
        request2.onload = () => {};
        request2.send();
      }
      
      if (
        (user_id_list.includes(` ${user_name.value} `)) &&
        password_list.includes(` ${pass_word.value} `)
        ) {
          sendInfo();
        } else {
          alert("Wrong credentials!!!!!!");
        }
      }, 2000);
  }  
});
