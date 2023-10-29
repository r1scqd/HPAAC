const user = JSON.parse(localStorage.getItem('user'))

console.log(user)


const nameUser = document.getElementById('get__user')
const nameUserTwo = document.getElementById('user__name__two')
const roleUser = document.getElementById('get__user__role')
const logout = document.getElementById('logout')

const mainName = document.getElementById('main__user__name')
const mainStatus = document.getElementById('main__user__status')
const mainOrg = document.getElementById('main__user__org')




nameUser.innerText = `${user.first_name} ${user.middle_name} ${user.last_name}`
mainName.innerText = `Ваше ФИО: ${user.first_name} ${user.middle_name} ${user.last_name}`
nameUserTwo.innerText = `${user.first_name} ${user.middle_name}`
roleUser.innerText = `${user.role}`
mainOrg.innerText = `Ваша организация: ${user.organization.name}`

mainStatus.innerText = `Ваш статус работы: ${user.status}`



logout.addEventListener('click', () => {
    localStorage.removeItem('user')
})

if (user.role == 'worker') {
    const applications = document.getElementById('applications').style.display = 'none'
    const trainingMaterialsDatabase = document.getElementById('training__materials__database').style.display = 'none'
    const testDatabase = document.getElementById('test__database').style.display = 'none'
    const employeeBase = document.getElementById('employee__base').style.display = 'none'
    const companyAnalytics = document.getElementById('company__analytics').style.display = 'none'
}