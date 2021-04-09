function confirmFunction() {
    response = confirm("Are you sure you want to sign up for this quest?");
    if (response)
    {
      return true;
    }
    else
    {
      return false;
    }
  }