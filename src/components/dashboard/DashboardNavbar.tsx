import React, { useCallback } from "react"
import { styled } from "@mui/material/styles"
import { AppBar, Box, Button, IconButton, Toolbar, Tooltip } from "@mui/material"
import { toast } from "react-toastify"
import { useRouter } from "next/router"
import { useUser } from "@/lib/hooks/useUser"
import ExitToAppIcon from "@mui/icons-material/ExitToApp"
import Link from "next/link"

const DashboardNavbarRoot = styled(AppBar)(({ theme }) => ({
  backgroundColor: theme.palette.background.paper,
  boxShadow: theme.shadows[3],
}))

interface IProps {
  onSidebarOpen: () => void
}

export const DashboardNavbar = ({ onSidebarOpen }: IProps) => {
  const { mutate } = useUser()
  const router = useRouter()

  const onSignOut = useCallback(async () => {
    toast.success("You have been signed out")
    mutate({ payload: null })
    router.replace("/")
  }, [mutate, router])

  return (
    <>
      <DashboardNavbarRoot>
        <Toolbar
          disableGutters
          sx={{
            minHeight: 64,
            left: 0,
            px: 2,
          }}
        >
          <Link href="/home" passHref>
            <Button color="inherit">Nearest Sea</Button>
          </Link>
          <Link href="/home1" passHref>
            <Button color="inherit">Distance to Sun</Button>
          </Link>
          <Box sx={{ flexGrow: 1 }} />
          <Tooltip title="Sign out">
            <IconButton onClick={onSignOut} sx={{ ml: 1 }}>
              <ExitToAppIcon />
            </IconButton>
          </Tooltip>
        </Toolbar>
      </DashboardNavbarRoot>
    </>
  )
}