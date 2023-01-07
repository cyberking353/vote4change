let regInput = document.querySelector('#reg');
let regMsg = document.querySelector('#reg-msg');
let psswd1 = document.querySelector('#password1');
let pssdMsg = document.querySelector('#psswd1-msg');
let pssdMsg2 = document.querySelector('#psswd2-msg');
let psswd2 = document.querySelector('#password2');
let btn  = document.querySelector('#btn');


regInput.addEventListener('blur',(e)=>{
    targetEl = e.target
    if(targetEl.value.length < 14){
        targetEl.nextSibling.classList.remove('validation');
        regMsg.innerHTML = '<p>Invalid Matriculation Number</p>';
        regMsg.className = "alert alert-danger"
        btn.disabled = true;
        
    }
    else{
        targetEl.nextSibling.classList.add('validation');
        regMsg.innerHTML = '';
        regMsg.className = ""
        btn.disabled = false;
        
    }
},false)


psswd1.addEventListener('input', (e)=>{
    targetEl = e.target;
    let regExpWeak = /[a-z]/;
    let regExpMedium = /\d+/;
    let regExpStrong = /.[!,@,#,$,%,^,&,*,?,_,~,-,(,)]/;
    let minWeakPsswd = 3;
    let minMediumPsswd = 6;
    let minStrongPsswd = 6;
    let inputWeakPsswd = targetEl.value.match(regExpWeak);
    let inputMediumPsswd = targetEl.value.match(regExpMedium);
    let inputStrongPsswd = targetEl.value.match(regExpStrong);

    if(targetEl.value){
        if(targetEl.value.length <= minWeakPsswd && (inputWeakPsswd || inputMediumPsswd || inputStrongPsswd)){
            targetEl.nextSibling.classList.remove('validation'); 
            pssdMsg.innerHTML = '<p>Weak Password</p>';
            btn.disabled = true;
        }
        
        if(targetEl.value.length >= minMediumPsswd && ((inputWeakPsswd && inputMediumPsswd) || (inputMediumPsswd && inputStrongPsswd) || (inputWeakPsswd && inputStrongPsswd))){
            targetEl.nextSibling.classList.add('validation'); 
            pssdMsg.innerHTML = '<p>Medium Password</p>'; 
            btn.disabled = false;
        }
        
        if(targetEl.value.length >= minStrongPsswd && inputWeakPsswd && inputMediumPsswd && inputStrongPsswd){
            targetEl.nextSibling.classList.add('validation'); 
            pssdMsg.innerHTML = '<p>Strong Password</p>'; 
            btn.disabled = false;
        }
    }

})


psswd2.addEventListener('input',(e)=>{
    targetEl = e.target
    if(targetEl.value != psswd1.value){
        targetEl.nextSibling.classList.remove('validation');
        pssdMsg2.innerHTML = '<p>Passwords Does Not Match!</p>';
        btn.disabled = true;
    }

    else {
        targetEl.nextSibling.classList.add('validation');
        pssdMsg2.innerHTML = '';
        btn.disabled = false ;
    }

})
