import { DashboardLayout } from "@/components/dashboard/DashboardLayout"
import Home1 from "@/components/dashboard/Home1"
import { useUser } from "@/lib/hooks/useUser"
import { Container, CircularProgress } from "@mui/material"
import Head from "next/head"
import React from "react"

const HomePage1 = () => {
  const { data } = useUser()

  if (!data?.payload) {
    return (
      <Container>
        <CircularProgress />
      </Container>
    )
  }

  return (
    <>
      <DashboardLayout>
        <Head>
          <title>{`Dashboard | ${data?.payload?.name}`}</title>
        </Head>
        <Home1 />
      </DashboardLayout>
    </>
  )
}

export default HomePage1
