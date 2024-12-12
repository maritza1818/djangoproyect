import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DiscotecasListComponent } from './discotecas-list.component';

describe('DiscotecasListComponent', () => {
  let component: DiscotecasListComponent;
  let fixture: ComponentFixture<DiscotecasListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DiscotecasListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DiscotecasListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
