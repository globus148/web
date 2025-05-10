def main():
    db_name = input().strip()
    global_init(db_name)
    db_sess = create_session()

    colonists = db_sess.query(User).filter(
        User.address == "module_1", User.age < 21).all()
    for i in colonists:
        i.address = 'module_3'
    db_sess.commit()
    db_sess.close()


if __name__ == "__main__":
    main()
