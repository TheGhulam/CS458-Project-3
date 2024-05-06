import nextConnect from "next-connect"
import auths from "../../../lib/middlewares/auth"

import { type Response } from "../../../types/response"
import { type NextApiRequest, type NextApiResponse } from "next"
import { handleAPIError, handleAPIResponse } from "../../../lib/utils"
import { type UserModelSchemaType, UserRegistrationSchema, UserModelSchema } from "../../../schema/UserSchema"

const handler = nextConnect<NextApiRequest, NextApiResponse<Response<UserModelSchemaType | null>>>()

handler.post(...auths, async (req, res) => {
})

export default handler
