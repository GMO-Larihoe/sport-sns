<template>
    <!-- <div class="login"> -->
      <!-- メールアドレス -->
      <!-- <div class="mail">
        <input type="email" v-model="email" placeholder="メール">
      </div> -->
  
      <!-- パスワード -->
      <!-- <div class="pass">
        <input type="password" v-model="password" placeholder="パスワード">
      </div> -->
  
      <!-- ログインボタン -->
      <!-- <div class="button">
        <button class="btn btn-primary" @click="login">ログイン</button>
      </div> -->
  
      <!-- 新規登録 -->
      <!-- <div class="new">
          <a href="/signup">新規登録</a>
      </div>
    </div>  -->
    <div class="login">
  <div class="login-triangle"></div>
  
  <h2 class="login-header">Log in</h2>

  <form class="login-container">
    <p><input type="email" placeholder="Email"></p>
    <p><input type="password" placeholder="Password"></p>
    <p><input type="submit" value="Log in"></p>
  </form>
</div>

  </template>

<script>

import axios from 'axios'; 
import router from './router/router.js'
export default {
    data() {
        return {
        email: "",
        password: "",
        };
    },
    setup(){
        
    },
    mounted() {
        

    },
    methods: {
        login: async function(){
            const params = new URLSearchParams();
            params.append('username', this.email);    // 渡したいデータ分だけappendする
            params.append('password', this.password);
            let config = {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            };
            let url = process.env.VUE_APP_API_DEV + '/token';
            const response = await axios.post(url, params, config);
            console.log("response.data = ", response.data)
            sessionStorage.setItem('access_token', response.data.access_token);
            router.push('/home')
        },
        newacount:function(){
          ('form').animate({height: "toggle", opacity: "toggle"}, "slow");
        },
        
    },
}

 </script>

<style scoped>
 @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700);

body {
  background-color: #456;
  font-family: 'Open Sans', sans-serif;
}

.login {
  width: 400px;
  margin: 16px auto;
  font-size: 16px;
}

/* Reset top and bottom margins from certain elements */
.login-header,
.login p {
  margin-top: 0;
  margin-bottom: 0;
}

/* The triangle form is achieved by a CSS hack */
.login-triangle {
  width: 0;
  margin-right: auto;
  margin-left: auto;
  border: 12px solid transparent;
  border-bottom-color: #ff9f04d5;
}

.login-header {
  background: #ff9f04d5;
  padding: 20px;
  font-size: 1.4em;
  font-weight: normal;
  text-align: center;
  text-transform: uppercase;
  color: #fff;
}

.login-container {
  background: #ebebeb;
  padding: 12px;
}

/* Every row inside .login-container is defined with p tags */
.login p {
  padding: 12px;
}

.login input {
  box-sizing: border-box;
  display: block;
  width: 100%;
  border-width: 1px;
  border-style: solid;
  padding: 16px;
  outline: 0;
  font-family: inherit;
  font-size: 0.95em;
}

.login input[type="email"],
.login input[type="password"] {
  background: #fff;
  border-color: #bbb;
  color: #555;
}

/* Text fields' focus effect */
.login input[type="email"]:focus,
.login input[type="password"]:focus {
  border-color: #888;
}

.login input[type="submit"] {
  background: #ff9f04d5;
  border-color: transparent;
  color: #fff;
  cursor: pointer;
}

.login input[type="submit"]:hover {
  background: #ff9f04d5;
}

/* Buttons' focus effect */
.login input[type="submit"]:focus {
  border-color: #ff9f04d5;
}
</style> 