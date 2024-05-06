import nextConnect from "next-connect"
import auths from "../../../lib/middlewares/auth"
import { type NextApiRequest, type NextApiResponse } from "next"

import { type Response } from "../../../types/response"
import { handleAPIError, handleAPIResponse } from "../../../lib/utils"

import { UserModelSchema, type UserModelSchemaType } from "../../../schema/UserSchema"

const handler = nextConnect<NextApiRequest, NextApiResponse<Response<Omit<UserModelSchemaType, "password"> | null>>>()

handler.use(...auths)

handler.get(async (req, res) => {
  const parsedData = UserModelSchema.omit({ password: true }).safeParse(req.user)

  if (!parsedData.success) {
    return handleAPIError(res, "Error getting user")
  }
  !parsedData.data ? handleAPIResponse(res, null, "No user found") : handleAPIResponse(res, parsedData.data, "User found")
})

handler.delete(async (req, res) => {
  if (!req.user) {
    handleAPIResponse(res, null, "No user found")
    return
  }
})

handler.patch(async (req, res) => {
  if (!req.user) {
    handleAPIResponse(res, null, "No user found")
    return
  }
})

export default handler
