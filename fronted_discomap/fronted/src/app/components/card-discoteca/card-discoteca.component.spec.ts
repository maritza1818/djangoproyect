import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardDiscotecaComponent } from './card-discoteca.component';

describe('CardDiscotecaComponent', () => {
  let component: CardDiscotecaComponent;
  let fixture: ComponentFixture<CardDiscotecaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardDiscotecaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CardDiscotecaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
