<template>
    <!-- <div class="m-5 text-center">
      <p class="m-1">氏名を入力してください。</p>
       名前 
      <div class="m-1">
        <input type="text" v-model="name" placeholder="氏名" />
        <p v-if="!isValidName && isNameTyped" class="error">
          有効な氏名を入力してください
        </p>
      </div>
  
       email 
      <div class="m-1">
        <input type="text" v-model="email" placeholder="email" />
      </div>
  
      <p class="m-1">
        新しいパスワードを入力してください。
        （大文字小文字を含む8文字以上24文字以内で入力してください）
      </p>
       新しいパスワード 
      <div class="m-1">
        <input type="password" v-model="password" placeholder="パスワード" />
        <p v-if="!isValidPasswd && isPasswdTyped" class="error">
          有効なパスワードを入力してください
        </p>
      </div>
  
     新しいパスワード（確認） 
      <div class="m-1">
        <input
          type="password"
          v-model="confirmation"
          placeholder="パスワード（確認）"
        />
        <p v-if="!isValidPWConfirm && isPWConfirmTyped" class="error">
          パスワードが一致しません
        </p>
      </div>
  
       ボタン 
      <div class="m-3">
        <button
          class="btn btn-primary"
          @click="signup"
        >
          登録
        </button>
      </div>
    </div> -->

    <!--追加したところ!!!!!lここいじる まだCSS追加してない-->
    
    <div class="login-page">
  <div class="form">
<div class="register-form">

      <input type="text" v-model="name" placeholder="name"/>
      <p v-if="!isValidName && isNameTyped" class="error">
      有効な氏名を入力してください
    </p>
      
      <input type="text" v-model="email" placeholder="email address"/>


      <input type="password" v-model="password" placeholder="password"/>
      <p v-if="!isValidPasswd && isPasswdTyped" class="error">
        有効なパスワードを入力してください
      </p>
      
      <input type="password" v-model="confirmation" placeholder="password(confirmation)"/>
      <p v-if="!isValidPWConfirm && isPWConfirmTyped" class="error">
        パスワードが一致しません
      </p>
    
      <button class="btn btn-primary" @click="signup">create</button>
      <p class="message">Already registered?
         <a href="/login">Sign In</a></p>
        

      </div>
  </div>
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
        name: "",
        };
    },
    setup(){
        
    },
    mounted() {
        

    },
    methods: {
        signup: async function(){
            let url = process.env.VUE_APP_API_DEV + '/provisional_signup';
            const response = await axios.post(url, {email: this.email, name: this.name, hashed_password: this.password});
            console.log("response.data = ", response.data)
            router.push('/login')
        },
        
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

 
 /* .form .register-form {
   display: none;
 } */

 
 /* .container {
   position: relative;
   z-index: 1;
   max-width: 300px;
   margin: 0 auto;
 } */
 
 
 /* .container:before, .container:after {
   content: "";
   display: block;
   clear: both;
 } */
 
 
 /* .container .info {
   margin: 50px auto;
   text-align: center;
 } */
 
 
 /* .container .info h1 {
   margin: 0 0 15px;
   padding: 0;
   font-size: 36px;
   font-weight: 300;
   color: #1a1a1a;
 } */
 
 
 /* .container .info span {
   color: #4d4d4d;
   font-size: 12px;
 } */
 /* .container .info span a {
   color: #000000;
   text-decoration: none;
 } */
 /* .container .info span .fa {
   color: #EF3B3A;
 } */
 
 
 body {
   background: #76b852; 
   background: rgb(141,194,111);
   background: linear-gradient(90deg, rgba(141,194,111,1) 0%, rgba(118,184,82,1) 50%);
   font-family: "Roboto", sans-serif;
   -webkit-font-smoothing: antialiased;
   -moz-osx-font-smoothing: grayscale;      
 } 
 
 </style> 