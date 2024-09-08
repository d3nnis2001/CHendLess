<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-900">
    <div class="bg-gray-800 p-8 rounded-lg shadow-md w-full max-w-md">
      <div class="text-center mb-8">
        <i class="text-4xl text-purple-500 mb-4">●</i>
        <h2 class="text-2xl font-semibold text-gray-100 mb-2">Forgot Password</h2>
        <p class="text-gray-400">Enter your email to reset your password</p>
      </div>
      <form @submit.prevent="handleResetPassword">
        <div class="mb-6">
          <label for="email" class="block text-gray-300 font-medium mb-2">Email</label>
          <input
              id="email"
              v-model="email"
              type="email"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <button
            type="submit"
            class="w-full bg-purple-600 text-white py-2 px-4 rounded-md hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:ring-offset-gray-800"
        >
          Reset Password
        </button>
      </form>
      <div class="text-center mt-6">
        <router-link to="/login" class="text-purple-400 hover:underline">Back to Login</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toast-notification'

const router = useRouter()
const toast = useToast()

const email = ref("")

const handleResetPassword = async () => {
  // Add your password reset logic here
  // For now, we'll just show a success message
  toast.success('Password reset email sent!', {
    timeout: 3000
  });
  router.push('/login')
};
</script>