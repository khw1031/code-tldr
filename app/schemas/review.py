from pydantic import BaseModel
from typing import Literal

# https://support.atlassian.com/bitbucket-cloud/docs/event-payloads/

class Account(BaseModel):
  username: str
  display_name: str
  account_id: str
  
class Repository(BaseModel):
  name: str

class Branch(BaseModel):
  name: str

class PullRequest(BaseModel):
  id: int
  title: str
  description: str
  state: Literal["OPEN", "MERGED", "DECLINED"]
  destination: Branch
  reviewers: list[Account]

class Content(BaseModel):
  raw: str
  markup: str
  html: str

class Comment(BaseModel):
  id: int
  parent: int
  content: Content

class Review(BaseModel):
  actor: Account
  repository: Repository
  pull_request: PullRequest
  comment: Comment
  
