def get_thread_name(user1_id, user2_id):
    name = f'{user1_id}-{user2_id}' if user1_id < user2_id else f'{user2_id}-{user1_id}'
    return 'chat_%s' % name
