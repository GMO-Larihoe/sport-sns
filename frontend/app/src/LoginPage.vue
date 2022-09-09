<template>
    <!-- <div class="login"> 
       メールアドレス 

      <div class="mail">
        <input type="email" v-model="email" placeholder="メール">
      </div>
  
       パスワード 
      <div class="pass">
        <input type="password" v-model="password" placeholder="パスワード">
      </div>
  
       ログインボタン 
      <div class="button">
        <button class="btn btn-primary" @click="login">ログイン</button>
      </div>
  
       新規登録 
      <div class="new">
          <a href="/signup">新規登録</a>
      </div>
    </div>  -->
      <div class="login-page">
  <div class="form">
  

    <!--新しく登録したところ-->
    <div class="login">
      <div class="mail">
      <input type="email" v-model="email" placeholder="email"/>
    </div>
    
    <div class="pass">
      <input type="password" v-model="password" placeholder="password"/>
    </div>
    <div class="button">
      <button class="btn btn-primary" @click="login">login</button>
    </div>

      <p class="message">Not registered? 
        <a href="/signup" >Create an account</a>
      </p>
    </div>
   </div>
</div>  
      <!-- ログインボタン -->
      <div class="button mt-1">
        <button class="btn btn-secondary" @click="login">ログイン</button>
      </div>
  
      <!-- 新規登録 -->
      <div class="new mt-1">
          <a href="/signup">新規登録</a>
      </div>
    </div>

<!--
    <div class="login">
  <div class="login-triangle"></div>
  
  <h2 class="login-header">Log in</h2>

  <form class="login-container">
    <p><input type="email" v-model="email" placeholder="Email"></p>
    <p><input type="password" v-model="password" placeholder="Password"></p>
    <p><button class="btn btn-primary" @click="login">ログイン</button></p>
  </form>
</div>
-->

  </template>

<script>

import axios from 'axios'; 
import router from './router/router.js'
//import { useRouter } from "vue-router"
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
            console.log(this.password)
            const params = new URLSearchParams();
            params.append('username', this.email);    // 渡したいデータ分だけappendする
            params.append('password', this.password);
            let config = {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            };
            let url = process.env.VUE_APP_API_DEV + '/token';

            axios.post(url, params, config).then(res =>{
              sessionStorage.setItem('access_token', res.data.access_token);
              router.push('/')
            });
        },

        newacount:function(){
          ('form').animate({height: "toggle", opacity: "toggle"}, "slow");

            
            

        },
//         $('.message a').click(function(){
//    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
// });



    },
}

 </script>

<style scoped>
 @import url(https://fonts.googleapis.com/css?family=Roboto:300);

.login-page {
  width: 360px;
  padding: 8% 0 0;
  margin: auto;
}
.form {
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 360px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.form input {
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #4CAF50;
  width: 100%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form button:hover,.form button:active,.form button:focus {
  background: #43A047;
}
.form .message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}
.form .message a {
  color: #4CAF50;
  text-decoration: none;
}
.form .register-form {
  display: none;
}
.container {
  position: relative;
  z-index: 1;
  max-width: 300px;
  margin: 0 auto;
}
.container:before, .container:after {
  content: "";
  display: block;
  clear: both;
}
.container .info {
  margin: 50px auto;
  text-align: center;
}
.container .info h1 {
  margin: 0 0 15px;
  padding: 0;
  font-size: 36px;
  font-weight: 300;
  color: #1a1a1a;
}
.container .info span {
  color: #4d4d4d;
  font-size: 12px;
}
.container .info span a {
  color: #000000;
  text-decoration: none;
}
.container .info span .fa {
  color: #EF3B3A;
}
body {
  background: #76b852; /* fallback for old browsers */
  background: rgb(141,194,111);
  background: linear-gradient(90deg, rgba(141,194,111,1) 0%, rgba(118,184,82,1) 50%);
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;      
}
</style> 