import bcrypt from "bcryptjs"
import { Db, ObjectId } from "mongodb"

export const findUserForAuth = async (db: Db, userId: string) => {
  const user = await db.collection("users").findOne({ _id: new ObjectId(userId) }, { projection: { password: 0 } })
  return user
}

export const findUserById = async (db: Db, userId: string) =>
  await db
    .collection("users")
    .findOne({ _id: new ObjectId(userId) }, { projection: { password: 0 } })
    .then((user) => user || null)

export const findUserWithEmailAndPassword = async (db: Db, email: string, password: string) => {
  const user = await db.collection("users").findOne({ email })
  if (user && (await bcrypt.compare(password, user.password))) {
    return { ...user }
  }
  return null
}

export const findUserByEmail = async (db: Db, email: string) =>
  await db
    .collection("users")
    .findOne({ email })
    .then((user) => user || null)

export const updateUserPasswordByOldPassword = async (db: Db, id: ObjectId, oldPassword: string, newPassword: string) => {
  const user = await db.collection("users").findOne(new ObjectId(id))
  if (!user) {
    return false
  }

  const matched = await bcrypt.compare(oldPassword, user.password)

  if (!matched) {
    return false
  }

  const password = await bcrypt.hash(newPassword, 10)

  await db.collection("users").updateOne({ _id: new ObjectId(id) }, { $set: { password } })
  return true
}

export const resetUserPassword = async (db: Db, id: string, newPassword: string) => {
  const password = await bcrypt.hash(newPassword, 10)
  await db.collection("users").updateOne({ _id: new ObjectId(id) }, { $set: { password } })
}

export const deleteUser = async (db: Db, id: ObjectId) => {
  await db.collection("users").deleteOne({ _id: new ObjectId(id) })
}