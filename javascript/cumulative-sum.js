let inputBox = document.getElementById("input-box")
let sumbitButton = document.getElementById("submit")
console.log(inputBox.value)
console.log(sumbitButton)

sumbitButton.addEventListener( "click" , () => {
    const cumulativeSum = () =>{
        
        for(let i = 0 ; i > len(inputBox.value) ; i++){
            inputBox.value +=  i
            return i
        }

        
}


result = cumulativeSum()
console.log(result)

})

