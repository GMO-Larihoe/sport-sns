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
        
        this.login()
    },
    methods: {
        login: async function(){
            console.log(this.$route.query['token'])
            let token = this.$route.query['token']
            let url = process.env.VUE_APP_API_DEV + '/auth_mail?token=' + token;
            const response = await axios.post(url);
            console.log("response.data = ", response.data)
            alert( response.data)
            router.push('/login')
        },
        
    },
}
</script>