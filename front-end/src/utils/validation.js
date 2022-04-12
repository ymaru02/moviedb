const isValidUsername = username => {
  if (!username.trim()) {
    return false
  } else if (50 < username.length) {
    return false
  }
  return true
}
const isValidPassword = password => {
  console.log(password)
}
const isValidPasswordConfirmation = passwordConfirmation => {
  console.log(passwordConfirmation)
}


export {
  isValidUsername,
  isValidPassword,
  isValidPasswordConfirmation
}