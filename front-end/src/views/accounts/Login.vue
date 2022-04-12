<template>
  <div class="login_box blurEffect"
    :style="{ backgroundImage: 'url(' + require('@/assets/background3.jpg') + ')' }"  >
    <div>
      <form @submit="login">
        <div class="input-box">
          <input id="username" type="text" class="font" name="username" placeholder="아이디" v-model="username">
          <label for="username ">아이디</label> 
        </div> 
        <div class="input-box">
          <input id="password" type="password" class="font" name="password" placeholder="비밀번호" v-model="password">
          <label for="password">비밀번호</label> 
        </div> 
        <div id="forgot">비밀번호 찾기</div>
        <input class="submit-btn" type="submit" value="로그인">
      </form>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Login',
  data: function () {
    return {
      username: '',
      password: '',
    }
  },
  components: {
  },
  computed: {
    ...mapState(['movieCards']),
  },
  methods: {
    login: function (event) {
      event.preventDefault()
      const payload = {
        username: this.username,
        password: this.password,
      }
      this.$store.dispatch('getToken', payload)
    }
  }
}
</script>

<style scoped>
  .login_box {
    height: 800px;
    /* width: 90%; */
    background-size: 100%;
    background-position: center;
    background-repeat: repeat-x;
    border: 1px solid #000000;
    animation: movebg 100s linear infinite ;
  }

  @keyframes movebg {
    0% { background-position: 0 center;}
    100% { background-position: -9035px center;}
  }

  .blurEffect {
    /* filter: blur(2px);
    -webkit-filter: blur(1px);
    -moz-filter: blur(1px);
    -o-filter: blur(1px); */
  }

  .input-box { 
    position:relative;
    margin: 10px 500px; 
  }

  .input-box > input { 
    background:transparent;
    border:none;
    border-bottom: solid 1px #ccc;
    padding:20px 0px 5px 0px;
    font-size:14pt;
    width:100%;
  }

  input::placeholder { 
    color:transparent;
  }

  input:placeholder-shown + label { 
    color:#aaa;
    font-size:14pt;
    top:15px;
  }

  input:focus + label, label {
    color:#8aa1a1;
    font-size:10pt;
    pointer-events: none; 
    position: absolute; 
    left:0px; top:0px;
    transition: all 0.2s ease ; 
    -webkit-transition: all 0.2s ease;
    -moz-transition: all 0.2s ease;
    -o-transition: all 0.2s ease;
  }

  input:focus, input:not(:placeholder-shown) { 
    border-bottom: solid 1px #8aa1a1;
    outline:none;
  }

  .submit-btn {
    font-size: 14px;
    border: none;
    padding: 10px;
    width: 260px;
    background-color: #4a008f;
    margin-bottom: 30px;
    color: white;
  }

  .font {
    color: white;
  }
</style>