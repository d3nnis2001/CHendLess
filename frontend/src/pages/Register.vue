<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-900">
    <div class="bg-gray-800 p-8 rounded-lg shadow-md w-full max-w-md">
      <div class="text-center mb-8">
        <i class="text-4xl text-purple-500 mb-4">●</i>
        <h2 class="text-2xl font-semibold text-gray-100 mb-2">Create an Account</h2>
        <p class="text-gray-400">
          Already have an account?
          <router-link to="/login" class="text-purple-400 hover:underline">Sign in</router-link>
        </p>
      </div>
      <form @submit.prevent="handleRegister">
        <div class="mb-4">
          <label for="firstName" class="block text-gray-300 font-medium mb-2">First Name</label>
          <input
              id="firstName"
              v-model="firstName"
              type="text"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <div class="mb-4">
          <label for="lastName" class="block text-gray-300 font-medium mb-2">Last Name</label>
          <input
              id="lastName"
              v-model="lastName"
              type="text"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <div class="mb-4">
          <label for="email" class="block text-gray-300 font-medium mb-2">Email</label>
          <input
              id="email"
              v-model="email"
              type="email"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <div class="mb-4">
          <label for="password" class="block text-gray-300 font-medium mb-2">Password</label>
          <input
              id="password"
              v-model="password"
              type="password"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <div class="mb-4">
          <label for="confirmPassword" class="block text-gray-300 font-medium mb-2">Confirm Password</label>
          <input
              id="confirmPassword"
              v-model="confirmPassword"
              type="password"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <div class="mb-6">
          <label for="birthdate" class="block text-gray-300 font-medium mb-2">Birthdate</label>
          <input
              id="birthdate"
              v-model="birthdate"
              type="date"
              class="w-full px-3 py-2 bg-gray-700 text-gray-200 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
          />
        </div>
        <button
            type="submit"
            class="w-full bg-purple-600 text-white py-2 px-4 rounded-md hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:ring-offset-gray-800"
        >
          Register
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toast-notification'
import {signupUser} from "@/api/user.js";

const router = useRouter()
const toast = useToast()

const firstName = ref("")
const lastName = ref("")
const email = ref("")
const password = ref("")
const confirmPassword = ref("")
const birthdate = ref("")

const handleRegister = async () => {
  if (firstName !== "" && lastName !== "" && email !== "" && password !== "" && confirmPassword !== "" && birthdate !== "") {
    if (password.value === confirmPassword.value) {
      const response = signupUser(firstName.value, lastName.value, email.value, password.value, birthdate.value)
      toast.success('Registration successful!', {
        timeout: 3000
      });
      router.push('/login')
    } else {
      toast.error('Password did not match confirmation password!', {
        timeout: 3000
      });
    }
  }
};
</script>