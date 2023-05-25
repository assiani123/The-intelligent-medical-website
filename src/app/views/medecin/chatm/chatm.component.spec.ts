import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChatmComponent } from './chatm.component';

describe('ChatmComponent', () => {
  let component: ChatmComponent;
  let fixture: ComponentFixture<ChatmComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChatmComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChatmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
