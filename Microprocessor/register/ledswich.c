#include "main.h"

//풀업은 반대다!!!!!!!!!!!!!!

void Delay_Timer(uint32_t time) {
	for (; time > 0; time--) {
	}
}

void reset() {
	Delay_Timer(100000);
	GPIOA->BSRR |= 0x1 << 27 | 0x1 << 28; // PA11,PA12 리셋
	GPIOB->BSRR |= 0x1 << 27 | 0x1 << 28; // PB11,PB12 리셋
}

void set(i) {
	Delay_Timer(100000);

	switch (i) {
	case 1:
		GPIOA->BSRR |= 0x1 << 12; // LED set
		break;

	case 2:
		GPIOA->BSRR |= 0x1 << 11; // LED set
		break;

	case 3:
		GPIOB->BSRR |= 0x1 << 12;
		break;

	case 4:
		GPIOB->BSRR |= 0x1 << 11;
		break;
	}
}

int main() {
	RCC->APB2ENR |= 0x1c; //0x11<<2
	GPIOA->CRH &= ~(0x44000);
	GPIOA->CRH |= 0x11000; // A11,A12 output
	GPIOB->CRH &= ~(0x44000);
	GPIOB->CRH = 0x11000; // B11,B12 output

	GPIOC->CRH &= ~(0x4); // 0x1<<2
	GPIOC->CRH |= 0x8; // PC8 INTPUT
	GPIOC->ODR |= 0x1 << 8;

	uint8_t i = 1;

	while (1) {
		if (GPIOC->IDR & 0x1 << 8) {
			reset();
		} else {
			set(i);
			Delay_Timer(100000);
			reset();
			Delay_Timer(100000);
			i++;
			if (i == 5) {
				i = 1;
			}
		}
	}
}
