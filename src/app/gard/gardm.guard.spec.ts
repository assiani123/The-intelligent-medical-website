import { TestBed } from '@angular/core/testing';

import { GardmGuard } from './gardm.guard';

describe('GardmGuard', () => {
  let guard: GardmGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(GardmGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
