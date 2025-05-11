def main():
    db_name = input().strip()
    global_init(db_name)
    db_sess = create_session()
    dept = db_sess.query(Department).filter(Department.id == 1).first()
    department_users = dept.members.split(", ") if dept.members else []
    print(1)
    for user_id in department_users:
        user = db_sess.query(User).filter(User.id == int(user_id)).first()
        print(2)
        total_hours = 0
        jobs = db_sess.query(Jobs).filter(Jobs.colloborators.like(f"%{user_id}%")).all()
        print(3)
        for job in jobs:
            if job.work_size:
                total_hours += job.work_size

        if total_hours > 25:
            print(user.surname, user.name)
    db_sess.close()


if __name__ == "__main__":
    main()