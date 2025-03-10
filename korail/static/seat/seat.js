// 자바스크립트를 이용하여 버튼 클릭 시 active 클래스를 토글
const roomButtons = document.querySelectorAll('.room_btn');

roomButtons.forEach(button => {
    button.addEventListener('click', () => {
        // 기존 active 클래스 제거
        roomButtons.forEach(btn => btn.classList.remove('active'));
        // 클릭한 버튼에 active 클래스 추가
        button.classList.add('active');
    });
});

document.addEventListener("DOMContentLoaded", () => {
    // 총 승객 인원
    const totalPassengers = {{ total_psg }};
    let selectedSeats = 0;  // 선택된 좌석 수

    const seatButtons = document.querySelectorAll('.seat_btn');
    const reserveButton = document.getElementById('reserve_button');

    seatButtons.forEach(button => {
        button.addEventListener('click', () => {
            const seatImage = button.querySelector('.seat img');

            if (button.classList.contains('disabled')) {
                return;  // 예매 불가능한 좌석은 클릭할 수 없음
            }

            // 선택된 좌석 수가 총 승객 수에 도달했는지 체크
            if (seatImage.src.includes("{% static 'image/select_seat.gif' %}")) {
                // 이미 선택된 좌석이면 원래 이미지로 복원
                seatImage.src = "{% static 'image/seat.gif' %}";
                selectedSeats--;  // 선택된 좌석 수 감소
            } else {
                // 선택되지 않은 좌석은 선택된 이미지로 변경
                seatImage.src = "{% static 'image/select_seat.gif' %}";
                selectedSeats++;  // 선택된 좌석 수 증가
            }

            // 총 승객 수만큼 좌석이 선택되면 예약하기 버튼 활성화
            if (selectedSeats === totalPassengers) {
                reserveButton.disabled = false;  // 예약하기 버튼 활성화
            } else {
                reserveButton.disabled = true;  // 예약하기 버튼 비활성화
            }
        });
    });
});

