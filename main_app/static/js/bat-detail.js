const dateInput = document.getElementById('id_date')

const calendarTheme = {
	theme_color: '#282a36', 
	main_background:'#44475a',
	active_text_color: '#f8f8f2',
	inactive_text_color: 'rgba(248, 248, 242, 0.35)',
	picker_header: {
		active: '#bd93f9'
	},
	weekday: {
		foreground: '#6272a4' 
	},
	display: {
		foreground: '#ff5555'
	},
	date: {
		active: {
			picked: {
				background: '#ff5555'
			}
		},
		marcked: {
			foreground: '#53a6fa'
		}
	},
	button: {
		danger: {
			foreground: '#ff5555'
		},
		success: {
			foreground: '#bd93f9'
		}
	}
};

const picker = MCDatepicker.create({
  el: '#id_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
  theme: calendarTheme,
})

dateInput.addEventListener("click", (evt) => {
  picker.open()
})