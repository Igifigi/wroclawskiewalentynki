const other_user_id = JSON.parse(document.getElementById('json-other-user-id').textContent);
const my_username = JSON.parse(document.getElementById('json-my-username').textContent);
const my_user_full_name = JSON.parse(document.getElementById('my-user-full-name').textContent);
const says_translation = JSON.parse(document.getElementById('json-says-trans').textContent);
const cant_send = JSON.parse(document.getElementById('json-cant-send').textContent);

const scheme = window.location.protocol == "https:" ? "wss" : "ws";

const socket = new WebSocket(
    `${scheme}://${window.location.host}/ws/${other_user_id}/`
);

socket.onmessage = function(e){
    render_message(JSON.parse(e.data));
}

function render_message(data){
    document.querySelector('#chat-body').innerHTML +=
    `
    <blockquote ${data.username == my_username ? "answer" : ""}>
    <strong>${data.user_full_name}</strong> ${says_translation}:
    <hr/>
    ${data.message}
    </blockquote>
    `
    scroll_to_bottom();
}

function send_message(){
    if(cant_send)
        return;

    const message_input = document.querySelector('#message-input');
    const message = message_input.value;

    if(message == '')
        return;

    socket.send(JSON.stringify({
        'message': message,
        'username': my_username,
        'user_full_name': my_user_full_name,
    }))
        
    message_input.value = '';
}

document.querySelector('#send-message-button').onclick = function(e){
    send_message();
}

document.querySelector('#message-input').onkeydown = function(e){
    if(e.key == "Enter")
        send_message();
}

function scroll_to_bottom(){
    const div = document.getElementById('chat-body')
    div.scrollTop = div.scrollHeight;
}

window.scrollTo(0, document.body.scrollHeight);
scroll_to_bottom();
