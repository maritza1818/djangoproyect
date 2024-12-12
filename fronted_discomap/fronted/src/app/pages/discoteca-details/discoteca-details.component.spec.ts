import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DiscotecaDetailsComponent } from './discoteca-details.component';

describe('DiscotecaDetailsComponent', () => {
  let component: DiscotecaDetailsComponent;
  let fixture: ComponentFixture<DiscotecaDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DiscotecaDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DiscotecaDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
