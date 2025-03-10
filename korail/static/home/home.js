

// 편도, 왕복 선택
function showOneWay() {
  document.getElementById('oneWayDate').style.display = 'block';
  document.getElementById('roundTripDates').style.display = 'none';

  // 버튼에 active 클래스 추가
  document.getElementById('oneWayBtn').classList.add('active');
  document.getElementById('roundTripBtn').classList.remove('active');
}

function showRoundTrip() {
  document.getElementById('oneWayDate').style.display = 'block';
  document.getElementById('roundTripDates').style.display = 'block';

  // 버튼에 active 클래스 추가
  document.getElementById('roundTripBtn').classList.add('active');
  document.getElementById('oneWayBtn').classList.remove('active');
}

// 출발지와 도착지 전환
function switchLocations() {
  var departureLocation = document.getElementById('departureLocation').innerText;
  var arrivalLocation = document.getElementById('arrivalLocation').innerText;

  document.getElementById('departureLocation').innerText = arrivalLocation;
  document.getElementById('arrivalLocation').innerText = departureLocation;
}

// 지역 선택 모달 열기
function openLocationSelect(locationType) {
  document.getElementById('locationSelectModal').style.display = 'block';
  window.selectedLocationType = locationType;
}

// 지역 선택 모달 닫기
function closeLocationSelect() {
  document.getElementById('locationSelectModal').style.display = 'none';
}

// 지역 버튼 클릭 시
document.querySelectorAll(".region-btn").forEach(button => {
  button.onclick = function () {
    const selectedLocation = this.textContent; // 화면에 보일 지역 이름
    const selectedValue = this.getAttribute("data-value"); // 지역의 실제 값

    // 출발지와 도착지에 값 설정
    if (window.selectedLocationType === "departure") {
      document.getElementById("departureLocation").innerText = selectedLocation;
      document.getElementById("departureLocation").setAttribute("data-value", selectedValue); // 출발지에 value 설정

      // input태그에 value 값을 지역 이름으로 변경.
      // ID를 통해 요소를 가져옴
      const departureInput = document.getElementById("DepartureStation_Input");
      // name 속성을 설정
      departureInput.setAttribute("value", selectedLocation);
      console.log(departureInput.value);

    }
    else {
      document.getElementById("arrivalLocation").innerText = selectedLocation;
      document.getElementById("arrivalLocation").setAttribute("data-value", selectedValue); // 도착지에 value 설정

      // input태그에 value 값을 지역 이름으로 변경.
      // ID를 통해 요소를 가져옴
      const arrivalInput = document.getElementById("ArrivalStation_Input");
      // name 속성을 설정
      arrivalInput.setAttribute("value", selectedLocation);
      console.log(arrivalInput.value);
    }

    // 콘솔에 값 출력 (출발지, 도착지)
    const departureValue = document.getElementById("departureLocation").getAttribute("data-value");
    const arrivalValue = document.getElementById("arrivalLocation").getAttribute("data-value");

    // console.log("출발지 값:", departureValue); // 예: "seoul"
    // console.log("도착지 값:", arrivalValue); // 예: "busan"

    document.getElementById(window.selectedLocationType + "Location").style.color = "#000000"; // 색상 변경
    closeLocationSelect();
  };
});

// 지역 검색 기능
function filterLocations() {
  const searchInput = document.getElementById("searchBar").value.toLowerCase();
  const regionButtons = document.querySelectorAll(".region-btn");

  regionButtons.forEach(button => {
    const regionName = button.textContent.toLowerCase();
    if (regionName.includes(searchInput)) {
      button.style.display = "block";
    } else {
      button.style.display = "none";
    }
  });
}



const today = new Date();
const year = today.getFullYear();
const month = today.getMonth() + 1; // 월 (0부터 시작하므로 +1 필요)
const date = today.getDate();
const days = ["일", "월", "화", "수", "목", "금", "토"];
const day = days[today.getDay()]; // 요일 (0=일요일, 1=월요일, ...)

// 형식에 맞게 포맷팅
const formattedDate = `${year}년 ${month}월 ${date}일 (${day}요일)`;

// HTML 요소 업데이트
document.getElementById("Departure_Date").textContent = formattedDate;

const dateInput = document.getElementById("Departure_Date_Input");
    // name 속성을 설정
dateInput.setAttribute("value", formattedDate);

// 날짜 포맷 함수 (YYYY년 MM월 DD일 (요일) 형식)
function formatDateWithDay(dateString) {
  const date = new Date(dateString);  // 날짜 문자열을 Date 객체로 변환
  const daysOfWeek = ["일", "월", "화", "수", "목", "금", "토"];  // 요일 배열
  const dayOfWeek = daysOfWeek[date.getDay()];  // 해당 날짜의 요일을 구함
  const year = date.getFullYear();  // 년도
  const month = date.getMonth() + 1;  // 월 (0부터 시작하므로 1을 더함)
  const day = date.getDate();  // 일

  return `${year}년 ${month}월 ${day}일 (${dayOfWeek})`;  // "2024년 11월 22일 (토)" 형식으로 반환

}

// 날짜 선택 후, data-value에 날짜 값 저장
function applySelectedDate() {
  const selectedDate = document.getElementById('calendarDate').value;  // 선택된 날짜
  const formattedDate = formatDateWithDay(selectedDate);  // "YYYY년 MM월 DD일 (요일)" 형식으로 변환
  const type = document.getElementById('calendarDate').getAttribute('data-type');  // 'departure' 또는 'return'
    console.log("2")

  // 선택된 날짜를 data-value에 저장
  if (type === 'departure') {
    // document.getElementById('departureSelectedDate').textContent = formattedDate;
    // document.getElementById('departureSelectedDate').setAttribute('data-value', selectedDate);  // departure의 data-value에 날짜 값 저장




  }

  else if (type === 'return') {
    document.getElementById('returnSelectedDate').textContent = formattedDate;
    document.getElementById('returnSelectedDate').setAttribute('data-value', selectedDate);  // return의 data-value에 날짜 값 저장
  }

  // input태그에 value 값을 지역 이름으로 변경.
    // ID를 통해 요소를 가져옴
    const dateInput = document.getElementById("Departure_Date_Input");
    // name 속성을 설정
    dateInput.setAttribute("value", formattedDate);
    console.log(dateInput.value);
    console.log("1")

  // 모달 닫기
  closeCalendarModal();
}

// 페이지 로드 시 "YYYY년 MM월 DD일 (요일)" 텍스트로 표시
window.onload = function() {
  const departureDate = document.getElementById('departureSelectedDate');
  const returnDate = document.getElementById('returnSelectedDate');

  // 기본 텍스트는 "YYYY년 MM월 DD일 (요일)"
  // departureDate.textContent = "YYYY년 MM월 DD일 (요일)";
  // returnDate.textContent = "YYYY년 MM월 DD일 (요일)";
}

// 날짜 선택 모달 열기
function openCalendarModal(type) {
  document.getElementById('calendarModal').style.display = 'block';
  // 현재 선택된 날짜에 맞는 값을 모달에 반영
  // const selectedDate = type == 'departure' ? document.getElementById('departureSelectedDate').textContent : document.getElementById('returnSelectedDate').textContent;
  const selectedDate = document.getElementById('Departure_Date').textContent
  const formattedDate = selectedDate.slice(0, 10); // "2024-11-22" 형식으로 value 적용
  document.getElementById('calendarDate').value = formattedDate;
  // 날짜 타입을 구분하기 위해 data-type 설정
  document.getElementById('calendarDate').setAttribute('data-type', type);


}

// 날짜가 선택되면 텍스트 변경
function applySelectedDate() {
  const selectedDate = document.getElementById('calendarDate').value;  // 선택된 날짜
  const formattedDate = formatDateWithDay(selectedDate);  // "YYYY년 MM월 DD일 (요일)" 형식으로 변환
  const type = document.getElementById('calendarDate').getAttribute('data-type');  // 'departure' 또는 'return'

  // 가는 날 또는 오는 날에 날짜를 설정
  if (type === 'departure') {
    document.getElementById('Departure_Date').textContent = formattedDate;
  } else if (type === 'return') {
    document.getElementById('returnSelectedDate').textContent = formattedDate;
  }

  // input태그에 value 값을 지역 이름으로 변경.
    const dateInput = document.getElementById("Departure_Date_Input");
    dateInput.setAttribute("value", formattedDate);
    console.log(dateInput.value);

  // 모달 닫기
  closeCalendarModal();
}

// 모달 닫기
function closeCalendarModal() {
  document.getElementById('calendarModal').style.display = 'none';
}

// 승차권 인원 선택
let passengerCount = 1; // 초기 인원 설정
const passengerBar = document.getElementById("passenger-bar");

// 인원 선택 슬라이드 바 열기
function openPassengerBar() {
  passengerBar.style.transform = "translateY(0)"; // 열기
}

// 인원 선택 슬라이드 바 닫기
function togglePassengerBar() {
  passengerBar.style.transform = "translateY(100%)"; // 닫기
}

// 어른 수 증가
function increaseAdults() {
  var adultCount = document.getElementById("adult-count");
  adultCount.textContent = parseInt(adultCount.textContent) + 1;
  console.log("hi")
}

// 어른 수 감소
function decreaseAdults() {
  var adultCount = document.getElementById("adult-count");
  if (parseInt(adultCount.textContent) > 0) {
    adultCount.textContent = parseInt(adultCount.textContent) - 1;
  }
}

// 아이 수 증가
function increaseChildren() {
  var childCount = document.getElementById("child-count");
  childCount.textContent = parseInt(childCount.textContent) + 1;
}

// 아이 수 감소
function decreaseChildren() {
  var childCount = document.getElementById("child-count");
  if (parseInt(childCount.textContent) > 0) {
    childCount.textContent = parseInt(childCount.textContent) - 1;
  }
}

// 유아 수 조절
  function decreaseInfants() {
    let infantCount = parseInt(document.getElementById("infant-count").innerText);
    if (infantCount > 0) {
      document.getElementById("infant-count").innerText = infantCount - 1;
    }
  }

  function increaseInfants() {
    let infantCount = parseInt(document.getElementById("infant-count").innerText);
    document.getElementById("infant-count").innerText = infantCount + 1;
  }

  // 노인 수 조절
  function decreaseElderly() {
    let elderlyCount = parseInt(document.getElementById("elderly-count").innerText);
    if (elderlyCount > 0) {
      document.getElementById("elderly-count").innerText = elderlyCount - 1;
    }
  }

  function increaseElderly() {
    let elderlyCount = parseInt(document.getElementById("elderly-count").innerText);
    document.getElementById("elderly-count").innerText = elderlyCount + 1;
  }

  // 적용 버튼 클릭 시, 선택한 인원 수 반영
function applyPassengerCount() {
  var adultCount = document.getElementById("adult-count").textContent;
  var childCount = document.getElementById("child-count").textContent;
  var infantCount = document.getElementById("infant-count").textContent;
  var elderlyCount = document.getElementById("elderly-count").textContent;

  var openPassengerBtn = document.getElementById("open-passenger-btn");
  var selectedPassengerText = document.getElementById("selected-passenger-text");

  // 텍스트 업데이트
  selectedPassengerText.textContent = `어른 ${adultCount}명, 아이 ${childCount}명, 유아 ${infantCount}명, 노인 ${elderlyCount}명`;
  selectedPassengerText.style.color = "black"; // 텍스트 색을 검은색으로 설정
  passengerCNT = adultCount + "," + childCount + "," + infantCount + "," + elderlyCount

  console.log(passengerCNT)
  // input태그에 value 값을 지역 이름으로 변경.
    const passengerCNTInput = document.getElementById("Passenger_CNT_Input");
    passengerCNTInput.setAttribute("value", passengerCNT);
    console.log(passengerCNTInput.value);
  // 슬라이드 바 닫기
  togglePassengerBar();
}


  // 승차권 조회 버튼을 누를 때, 데이터를 폼에 넣는 함수
    function submitTicketForm() {

  // 출발지와 도착지
      document.getElementById('departureInput').value = document.getElementById('departureLocation').innerText;
      document.getElementById('arrivalInput').value = document.getElementById('arrivalLocation').innerText;

  // 날짜
      document.getElementById('departureDateInput').value = document.getElementById('departureSelectedDate').dataset.value;
      document.getElementById('returnDateInput').value = document.getElementById('returnSelectedDate').dataset.value;

  // 승객 수
      document.getElementById('adultCountInput').value = document.getElementById('adult-count').innerText;
      document.getElementById('childCountInput').value = document.getElementById('child-count').innerText;
      document.getElementById('infantCountInput').value = document.getElementById('infant-count').innerText;
      document.getElementById('elderlyCountInput').value = document.getElementById('elderly-count').innerText;

  // 폼 제출
      document.getElementById('ticketForm').submit();
    }


  // 편도 왕복
    function submitTicketForm() {
      const departure = document.getElementById('departureLocation').innerText;
      const arrival = document.getElementById('arrivalLocation').innerText;
      const departureDate = document.getElementById('departureSelectedDate').dataset.value;
      const returnDate = document.getElementById('returnSelectedDate').dataset.value;
      const adultCount = document.getElementById('adult-count').innerText;
      const childCount = document.getElementById('child-count').innerText;
      const infantCount = document.getElementById('infant-count').innerText;
      const elderlyCount = document.getElementById('elderly-count').innerText;

      const isRoundTrip = document.getElementById('roundTripBtn').classList.contains('active');

      if (isRoundTrip) {
        document.getElementById('roundTripDepartureInput').value = departure;
        document.getElementById('roundTripArrivalInput').value = arrival;
        document.getElementById('roundTripDepartureDateInput').value = departureDate;
        document.getElementById('roundTripReturnDateInput').value = returnDate;
        document.getElementById('roundTripAdultCountInput').value = adultCount;
        document.getElementById('roundTripChildCountInput').value = childCount;
        document.getElementById('roundTripInfantCountInput').value = infantCount;
        document.getElementById('roundTripElderlyCountInput').value = elderlyCount;
        document.getElementById('roundTripForm').submit();
      } else {
        document.getElementById('oneWayDepartureInput').value = departure;
        document.getElementById('oneWayArrivalInput').value = arrival;
        document.getElementById('oneWayDepartureDateInput').value = departureDate;
        document.getElementById('oneWayAdultCountInput').value = adultCount;
        document.getElementById('oneWayChildCountInput').value = childCount;
        document.getElementById('oneWayInfantCountInput').value = infantCount;
        document.getElementById('oneWayElderlyCountInput').value = elderlyCount;
        document.getElementById('oneWayForm').submit();
      }
    }

    function showOneWay() {
      document.getElementById('oneWayBtn').classList.add('active');
      document.getElementById('roundTripBtn').classList.remove('active');
      document.getElementById('roundTripDates').style.display = 'none';
      document.querySelector('.separator').style.display = 'none';
    }

    function showRoundTrip() {
      document.getElementById('roundTripBtn').classList.add('active');
      document.getElementById('oneWayBtn').classList.remove('active');
      document.getElementById('roundTripDates').style.display = 'block';
      document.querySelector('.separator').style.display = 'inline-block';
    }