<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-900">
    <div class="bg-gray-800 p-8 rounded-lg shadow-md w-full max-w-md">
      <div class="text-center mb-8">
        <!--TODO: Add logo here -->
        <i class="text-4xl text-purple-500 mb-4">●</i>
        <h2 class="text-2xl font-semibold text-gray-100 mb-2">Welcome Back</h2>
        <p class="text-gray-400">
          Don't have an account?
          <router-link to="/signup" class="text-purple-400 hover:underline">Create today!</router-link>
        </p>
      </div>
      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label for="email" class="block text-gray-300 font-medium mb-2">Email</label>
          <input
              id="email"
              v-model="emailInput"
              type="email"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-300 font-medium mb-2">Password</label>
          <input
              id="password"
              v-model="passwordInput"
              type="password"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center">
            <input
                id="rememberme"
                v-model="checkbox_remember"
                type="checkbox"
                class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-500 rounded bg-gray-700"
            />
            <label for="rememberme" class="ml-2 block text-gray-300">Remember me</label>
          </div>
          <router-link to="/forgot-password" class="text-purple-400 hover:underline">Forgot password?</router-link>
        </div>
        <button
            type="submit"
            class="w-full bg-purple-600 text-white py-2 px-4 rounded-md hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:ring-offset-gray-800"
        >
          Sign In
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toast-notification'
import { checkLogin } from "../api/user.js"

const router = useRouter()
const toast = useToast()

const emailInput = ref("")
const passwordInput = ref("")
const checkbox_remember = ref(false)

const handleLogin = async () => {
  try {
    const response = await checkLogin(emailInput.value, passwordInput.value);

    if (response.status === 200) {
      toast.success('You have successfully logged in!', {
        timeout: 3000
      });
      router.push('/dashboard')
    }
  } catch (error) {
    if (error.response) {
      toast.error(error.response.data.message || 'Invalid email or password', {
        timeout: 3000
      });
    } else if (error.request) {
      toast.error('Unable to connect to the server. Please check your internet connection.', {
        timeout: 3000
      });
    } else {
      toast.error('An unexpected error occurred. Please try again.', {
        timeout: 3000
      });
    }
  }
};
</script>