import Head from "next/head"
import Login from "@/components/auth/Login"
import { GoogleOAuthProvider } from "@react-oauth/google";

export default function Home() {
  return (
    <>
      <Head>
        <title>CS458 Software Verification and Validation</title>
      </Head>
      <Login />
    </>
  )
}
