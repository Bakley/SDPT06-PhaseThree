from repositories.member_repository import MemberRepository

class MemberService:
    def __init__(self):
        self.repository = MemberRepository()

    def add_member(self, name, email, join_date):
        self.repository.add_member(name, email, join_date)

    def list_members(self):
        return self.repository.list_members()

    def update_member(self, member_id, name, email):
        self.repository.update_member(member_id, name, email)

    def soft_delete_member(self, member_id):
        self.repository.soft_delete_member(member_id)
